import qrcode
import xml.etree.ElementTree as ET

from operator import getitem
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView, DeleteView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from bs4 import BeautifulSoup as Soup
from school.csv.csv_obj import Csv

# Домашняя страница
class FirsPage(ListView):
    template_name = 'home.html'
    
    def observe(request): 
        return render(request, 'home.html')

# Страница авторизации 
class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main_page.html'

    def get_success_url(self):
        return reverse_lazy('table')

# Онавление данных путум чтения или изменения CSV файлов
class Upload(ListView):
    model = File
    template_name = 'simple_upload.html'
    context_object_name = 'upload'
   
    def save_in_csv(request):
        users = Accounting.objects.all()
        dataSet = []
        
        for i in users:
            row = []
            
            row.append(str(i.users))
            row.append(str(i.technincs))
            row.append(str(i.create))
            row.append(str(i.tecNumber))
            
            dataSet.append(row)
            
        csv = Csv()
        err = csv.write_in_csv(dataSet=dataSet, path="mysite/static/csv/csv.csv")
        if err != 0:
            raise Exception("Запись прошла неудачно")
        
        return redirect("table")
    
    def simple_upload(request): 
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
                        
            if myfile.content_type != "text/csv":
                return HttpResponseNotFound('<h2>Uncorrect file</h2>')  
                     
            f = File()           
            f.title = request.POST.get('title')          
            f.file = request.FILES['myfile']           
            f.save()            
            return render(request, 'simple_upload.html')       
        return render(request, 'simple_upload.html')
       
    def read_from_csv(request, file):
        if request.method == 'GET':
            upload = File.objects.get(file = str(file))
            
            csv = Csv()
            csv_data = csv.read_csv(upload)
            
            for i in csv_data[1:]:
                svt = SVT()
                svt.name = i[0]
                svt.acounting = i[1]
                svt.inv_number = i[2]
                svt.cmo = i[3]
                svt.data_get = i[4]
                svt.data_inp = i[5]
                svt.quantity = i[6]
                svt.save()
                         
            return redirect("table")
    
    def all_csv(request):
        upload = File.objects.all()
        return render(request, 'read_from_xml.html', {'upload':upload})


# Страница книги учета   
class Table(ListView):
    model = Accounting
    template_name = 'build.html'
    context_object_name = 'acounting'
    
    def delete(request, id):
        try:
            user = Accounting.objects.get(id = id)
            user.delete()         
            return redirect('table')     
        except Accounting.DoesNotExist:          
            return HttpResponseNotFound('<h2>User not found</h2>')
        
    def update(request, id):
        try:
            user = Accounting.objects.get(id = id)
            user.delete()           
            if request.method == 'POST':
                user.users = request.POST.get('users')
                user.technincs = request.POST.get('technincs')
                user.tecNumber = request.POST.get('tecNumber')
                user.save()             
                return redirect('table')          
            else:
                return render(request, 'update_accounting.html')          
        except Accounting.DoesNotExist:
            return HttpResponseNotFound('<h2>Person not found</h2>')
        
    def find(request):
        search_query = request.GET.get('find','')     
        if search_query:
            people = Accounting.objects.filter(Q(tecNumber__icontains = search_query) \
                | Q(users__icontains = search_query) | Q(technincs__icontains = search_query))
        else:
            people = Accounting.objects.all       
        return render(request, "find.html", {'people':people})
    
    def save_in_csv(request):
        user_info = Accounting.objects.all() 
              
        date = []
       
        for i in user_info:
            arr = {}
            arr["user"] = str(i.users)
            arr["tec"] = str(i.technincs)
            arr["create"] = str(i.create)
            arr["tecNumber"] = str(i.tecNumber)
            date.append(arr)      
        table = ET.Element('table')

        for i, item in enumerate(date, 1):
            person = ET.SubElement(table, 'person' + str(i))
            ET.SubElement(person, 'user').text = item['user']
            ET.SubElement(person, 'tec').text = item['tec']
            ET.SubElement(person, 'create').text = item['create']
            ET.SubElement(person, 'tecNumber').text = item['tecNumber']     
                  
        mydate = ET.tostring(table, encoding="unicode")
        
        f = open("mysite/static/xml/xml.xml", "w")
        f.write(mydate)
        f.close()
        return redirect("table")
 

# Страница склада        
class Storage(ListView):
    model = SVT
    template_name = 'storage.html'
    context_object_name = 'store'

    def get_objects(request, count):
        if count == 50:
            nxt = count + 50
            prev = 50
            store = SVT.objects.all()[:count]
            return render(request, "storage.html", {"store": store, "next": nxt, "prev": prev})
        else:
            nxt = count + 50
            prev = count - 50
            store = SVT.objects.all()[prev+1:count+1]
            return render(request, "storage.html", {"store":store, "next": nxt, "prev": prev})

    def delete(request, id):
        try:
            technique = Store.objects.get(id=id)
            technique.delete()           
            return redirect('stor')       
        except Accounting.DoesNotExist:
            return HttpResponseNotFound('<h2>Technique not found</h2>')
        
    def update(request, id):
        try:
            technique = Store.objects.get(id=id)
            
            if request.method == 'POST':
                technique.technincs = request.POST.get('technincs')
                technique.tecNumber = request.POST.get('tecNumber')
                technique.status = request.POST.get('status')
                user.save()               
                return redirect('stor')            
            else:
                return render(request, 'update_storage.html')
        except Accounting.DoesNotExist:
            return HttpResponseNotFound('<h2>Person not found</h2>')
        
    def find(request):
        search_query = request.GET.get('find','')
        
        if search_query:
            obj = Store.objects.filter(Q(tecNumber__icontains = search_query) | Q(technincs__icontains = search_query))
        else:
            obj = Store.objects.all        
        return render(request, "find_storage.html", {'object':obj})
    
    def qr(request, id):
        obj = Store.objects.get(id=id)       
        data = "Техника:" + " " + str(obj.technincs) + "\n" + "Техномер:" + " " + str(obj.tecNumber) + "\n"
        data = data.encode("cp1251")
        filename = "qr" + str(id) +".png"
        img = qrcode.make(data)
        
        img.save("mysite/static/img/"+filename)
        
        filename = "/static/img/"+filename   
           
        return render(request, "qr.html", {'filename':filename})
    
    def drop(request):
        if request.method == 'POST':
            obj = SVT.objects.all().delete()
        return redirect("stor")
                 

# Добавление в книгу учета
class Add_accounting(CreateView):
    form_class =  AddAccountingForm
    template_name = 'add_accounting.html'
    context_object_name = 'add_acounting'
    success_url = reverse_lazy('table')

# Добавление предмета на склад   
class Add_storage(CreateView):
    form_class =  AddStorageForm
    template_name = 'add_storage.html'
    context_object_name = 'add_storage'
    success_url = reverse_lazy('stor')
    
            
    
    



     
    
    

 
