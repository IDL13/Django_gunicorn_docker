import qrcode
import smtplib
import os

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from django.shortcuts import redirect, render
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView
from django.db.models import Q
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

# Онавление данных путём чтения или изменения CSV файлов
class Upload(ListView):
    model = File
    template_name = 'simple_upload.html'
    context_object_name = 'upload'

    # Сохранение данных в CSV
    def save_in_csv(request):
        password = os.getenv("MAIL_PASS")
        users = SVT.objects.all()
        dataSet = []
        
        for i in users:
            row = []
            
            row.append(str(i.name))
            row.append(str(i.acounting))
            row.append(str(i.inv_number))
            row.append(str(i.ser_number))
            row.append(str(i.cmo))
            row.append(str(i.data_get))
            row.append(str(i.data_inp))
            row.append(str(i.quantity))
            
            dataSet.append(row)
        
        filename = "csv" + dataSet[0][2] + ".csv"
        path = "media/csv/" + filename

        csv = Csv()
        err = csv.write_in_csv(dataSet=dataSet, path="media/csv/"+filename)
        if err != 0:
            raise Exception("Запись прошла неудачно")
        
        if request.method == 'GET':
            return render(request, 'csv.html')
        if request.method == 'POST':
            mail = request.POST.get("mail")
            
            # Блок формирования письма с CSV файлом
            msg = MIMEMultipart()
            msg["Subject"] = "CSV"
            msg["From"] = "info@sch-mr.ru"

            part = MIMEApplication(open(path, "rb").read())
            part.add_header("Content-Disposition", "attachment", filename = filename)
            msg.attach(part)

            server = smtplib.SMTP("mail.sch-mr.ru", 587)
            server.login("info@sch-mr.ru", password)
            server.sendmail(msg['From'], mail, msg.as_string())

            return render(request, "storage.html")

    # Добавление файла в базу дынных (загрузка файла на сайт)  
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

    # Парсер CSV файла
    def read_from_csv(request, file):
        if request.method == 'GET':
            upload = File.objects.get(file = str(file))
            
            csv = Csv()
            csv_data = csv.read_csv(upload)
            
            # try:
            #     o = SVT.objects.get(inv_number="0101010101")
            # except:
            #     pass
            
            for i in csv_data[1:]:
                try:
                    inv = SVT.objects.get(inv_number=i[2])
                    continue
                except:
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
        
    # Список всех файлов из базы данных
    def all_csv(request):
        upload = File.objects.all()
        return render(request, 'read_from_xml.html', {'upload':upload})


# Страница книги учета  
class Table(ListView):
    model = Accounting
    template_name = 'build.html'
    context_object_name = 'acounting'

    # Удаление из учета по id
    def delete(request, id):
        try:
            user = Accounting.objects.get(id = id)
            user.delete()         
            return redirect('table')     
        except Accounting.DoesNotExist:          
            return HttpResponseNotFound('<h2>User not found</h2>')
    
    # Обновление записи учета по id  
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
     
    # Поиск по учету   
    def find(request):
        search_query = request.GET.get('school','')
        
        if search_query:
            obj = AcountingBook.objects.filter(Q(name__icontains=search_query) | Q(inv_number__icontains=search_query) |\
                                     Q(cmo__icontains=search_query))
        else:
            obj = AcountingBook.objects.all
        return render(request, "find.html", {'object': obj})

# Страница склада        
class Storage(ListView):
    model = SVT
    template_name = 'storage.html'
    context_object_name = 'store'

    # Получение 50 записей из склада
    def get_objects(request, count):
        if count == 50:
            nxt = count + 50
            prev = 50
            store = SVT.objects.all()[:count]
            return render(request, "storage.html", {"store": store, "next": nxt, "prev": prev})
        else:
            nxt = count + 50
            prev = count - 50
            store = SVT.objects.all()[prev:count]
            return render(request, "storage.html", {"store":store, "next": nxt, "prev": prev})

    # Удаление со склада
    def delete(request, id):
        try:
            technique = SVT.objects.get(id=id)
            technique.delete()           
            return redirect('stor')       
        except Accounting.DoesNotExist:
            return HttpResponseNotFound('<h2>Technique not found</h2>')
        
    # Обновленеи элемента склада  
    def update(request, id):
        try:
            svt = SVT.objects.get(id=id)   
            
            if request.method == 'POST':
                technique = SVT.objects.get(id=id)
                technique.name=request.POST.get('name')
                technique.acounting=request.POST.get('acounting')
                technique.inv_number=request.POST.get('inv_number')
                technique.ser_number=request.POST.get('ser_number')
                technique.cmo=request.POST.get('cmo')
                technique.data_get=request.POST.get('data_get')
                technique.data_inp=request.POST.get('data_inp')
                technique.quantity=request.POST.get('quantity')
                technique.save()
                return redirect('stor')           
            else:
                return render(request, "update_storage.html", {"svt": svt})
        except Accounting.DoesNotExist:
            return HttpResponseNotFound('<h2>Person not found</h2>')
    
    # Поиск по складу     
    def find(request):
        search_query = request.GET.get('find','')
        
        if search_query:
            obj = SVT.objects.filter(Q(name__icontains=search_query) | Q(inv_number__icontains=search_query) |\
                                     Q(cmo__icontains=search_query))
        else:
            obj = SVT.objects.all
        return render(request, "find_storage.html", {'object': obj})
    
    # Генератор QR кодов
    def qr(request, id):
        password = os.getenv("MAIL_PASS")
        filename = "qr" + str(id) +".png"
        path = "media/img/" + filename
        if request.method == "GET":
            obj = SVT.objects.get(id=id)
            data = "Техника:" + " " + str(obj.name) + "\n" + "Техномер:" + " " + str(obj.inv_number) + "\n"
            data = data.encode("cp1251")
            img = qrcode.make(data)

            img.save("media/img/" + filename)

            filename = "/media/img/" + filename
            
            return render(request, "qr.html", {'filename':filename})
        
        if request.method == "POST":
            mail = request.POST.get("mail")

            msg = MIMEMultipart()
            msg["Subject"] = "QRcode"
            msg["From"] = "info@sch-mr.ru"

            part = MIMEApplication(open(path, "rb").read())
            part.add_header("Content-Disposition", "attachment", filename = filename)
            msg.attach(part)

            server = smtplib.SMTP("mail.sch-mr.ru", 587)
            server.login("info@sch-mr.ru", password)
            server.sendmail(msg['From'], mail, msg.as_string())

            return render(request, "storage.html")

    # Сброс всех записей из SVT
    def drop(request):
        if request.method == 'POST':
            obj = SVT.objects.all().delete()
        return redirect("stor")
                 

# Добавление в книгу учета
class Add_accounting(CreateView):
    form_class = AddAccountingForm
    template_name = 'add_accounting.html'
    context_object_name = 'add_acounting'
    success_url = reverse_lazy('table')

# Добавление предмета на склад   
class Add_storage(CreateView):
    form_class = AddStorageForm
    template_name = 'add_storage.html'
    context_object_name = 'add_storage'
    success_url = reverse_lazy('stor')
    

# Класс миграции из склада в учет
class Migration(ListView):
    # Создание миграции
    def make_migration(request):
        old = SVT.objects.all()
        for i in range(len(old)):
            new = AcountingBook()
            new.name = old[i].name
            new.acounting = old[i].acounting
            new.cmo = old[i].cmo
            new.inv_number = old[i].inv_number
            new.ser_number = old[i].ser_number
            new.kab = 000
            new.quantity = old[i].quantity
            new.save()
        return render(request, "storage.html")

    # Удаление миграции
    def drop_migration(request):
        obj = AcountingBook.objects.all().delete()
        return render(request, "storage.html")
    
    # Обновление в мигрированной записи
    def update_acountingBook(request, id):
        try:
            svt = AcountingBook.objects.get(id=id)   
            
            if request.method == 'POST':
                technique = AcountingBook.objects.get(id=id)
                technique.name=request.POST.get('name')
                technique.acounting=request.POST.get('acounting')
                technique.inv_number=request.POST.get('inv_number')
                technique.ser_number=request.POST.get('ser_number')
                technique.cmo=request.POST.get('cmo')
                technique.kab=request.POST.get('kab')
                technique.quantity=request.POST.get('quantity')
                technique.save()
                return redirect('table')           
            else:
                return render(request, "update_book.html", {"svt": svt})
        except Accounting.DoesNotExist:
            return HttpResponseNotFound('<h2>Person not found</h2>')
    
    
            
    
    



     
    
    

 
