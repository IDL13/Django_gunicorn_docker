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

import xml.etree.ElementTree as ET
from django.core.files.storage import FileSystemStorage


class FirsPage(ListView):
    template_name = 'home.html'
    
    def observe(request):
        return render(request, 'home.html')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main_page.html'

    # def get_context_data(self, *, object_list = None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('table')

class Upload(ListView):
    model = File
    template_name = 'simple_upload.html'
    context_object_name = 'upload'

    def save_in_xml(request):
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

    # def simple_upload(request):
    #     if request.method == 'POST' and request.FILES['myfile']:
    #         title = request.POST.get('title')
    #         myfile = request.FILES['myfile']
    #         if myfile.content_type != "text/xml":
    #             return HttpResponseNotFound('<h2>Uncorrect file</h2>')

    #         model = Upload()
    #         mode.title = title
    #         model.file = myfile
            
    #         # fs = FileSystemStorage()
    #         # filename = fs.save(myfile.name, myfile)
    #         # uploaded_file_url = fs.url(filename)
    #         return render(request, 'simple_upload.html', {
    #             'uploaded_file_url': uploaded_file_url
    #         })
    #     return render(request, 'simple_upload.html')   
    
class Table(ListView):
    model = Accounting
    template_name = 'build.html'
    context_object_name = 'acounting'
    
    def delete(request, tec):
        try:
            user = Accounting.objects.get(tecNumber=tec)
            user.delete()
            return redirect('table')
        except Accounting.DoesNotExist:
            return HttpResponseNotFound('<h2>User not found</h2>')
        
    def update(request, tec):
        try:
            user = Accounting.objects.get(tecNumber=tec)
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
            people = Accounting.objects.filter(Q(tecNumber__icontains = search_query) | Q(users__icontains = search_query) | Q(technincs__icontains = search_query))
        else:
            people = Accounting.objects.all
        
        return render(request, "find.html", {'people':people})
    
    def save_in_xml(request):
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
        
    def simple_upload(request):
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            if myfile.content_type != "text/xml":
                return HttpResponseNotFound('<h2>Uncorrect file</h2>')
            f = open(myfile) 
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'simple_upload.html', {
                'uploaded_file_url': uploaded_file_url
            })
        return render(request, 'simple_upload.html')


class Storage(ListView):
    model = Store
    template_name = 'storage.html'
    context_object_name = 'store'

    def delete(request, tec):
        try:
            technique = Store.objects.get(tecNumber=tec)
            technique.delete()
            return redirect('storage')
        except Accounting.DoesNotExist:
            return HttpResponseNotFound('<h2>Technique not found</h2>')
        
    def update(request, tec):
        try:
            technique = Store.objects.get(tecNumber=tec)
            if request.method == 'POST':
                technique.technincs = request.POST.get('technincs')
                technique.tecNumber = request.POST.get('tecNumber')
                technique.status = request.POST.get('status')
                user.save()
                return redirect('storage')
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

    # def get_context_data(self, *, object_list = None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return dict(list(context.items())) 

    # def get_success_url(self):
    #     return reverse_lazy('add')    
        

class Add_accounting(CreateView):
    form_class =  AddAccountingForm
    template_name = 'add_accounting.html'
    context_object_name = 'add_acounting'
    success_url = reverse_lazy('table')

   
class Add_storage(CreateView):
    form_class =  AddStorageForm
    template_name = 'add_storage.html'
    context_object_name = 'add_storage'
    success_url = reverse_lazy('storage')
    
class Add_file(CreateView):
    form_class =  AddFileForm
    template_name = 'simple_upload.html'
    context_object_name = 'simple_upload'
    success_url = reverse_lazy('table')
            
    
    



     
    
    

 
