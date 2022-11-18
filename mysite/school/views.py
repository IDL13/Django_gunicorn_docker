from operator import getitem
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate


def input(request):
    if request.method == 'GET':
        form = AuthorizationForm()
        return render(request, 'base.html', {'form': form})
    else:
        adres = request.POST.get('adress')
        job = request.POST.get('jobtitle')
        log = request.POST.get('login')
        pas = request.POST.get('password')

        acounting = Accounting.objects.all()
        store = Store.objects.all()
        user = Castomer.objects.all()

<<<<<<< HEAD
        acounting = Accounting.objects.all()
        store = Store.objects.all()

        user = authenticate(request, login=log, password=pas)
        login(request, user)
        if adres == "1" and job == "1":
            return render(request, 'school/Okt_zavh.html', {'acounting': acounting, 'store': store})
        elif adres == "1" and job == "2":
            return render(request, 'school/Okt_admin.html', {'acounting': acounting, 'store': store})
        elif adres == "1" and job == "3":
            return render(request, 'school/Okt_HDR.html', {'acounting': acounting, 'store': store})
=======
        user_pass = user.filter(password = pas)
        user_log = user.filter(login = log)

        if len(user_pass) > 0:
            if adres == "1" and job == "1":
                return render(request, 'school/Okt_zavh.html', {'acounting': acounting, 'store': store})
            elif adres == "1" and job == "2":
                return render(request, 'school/Okt_admin.html', {'acounting': acounting, 'store': store})
            elif adres == "1" and job == "3":
                return render(request, 'school/Okt_HDR.html', {'acounting': acounting, 'store': store})
        else:
            return HttpResponse('Error. Invalid password')
>>>>>>> d8ec0c30d5ebeae68938dbdcf0e293fa57595192
        
def storege (request):
    if request.method == 'GET':
        store = StoreForm()
        store = Store.objects.all()
        return render(request, 'storege.html', {'store': store})
    else:
        return redirect('/')

def add(request):
    if request.method == "GET":
        add_inf = AddForm()
        return render(request, 'add.html', {"add": add_inf,} )
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            add = Accounting(
                users = form.cleaned_data['users'],
                technincs = form.cleaned_data['technincs'], 
                create = form.cleaned_data['create'],
                tecNumber = form.cleaned_data['tecNumber']
            )
            add.save()
            return redirect('/')


      
      
      
      
      
      
      
      
    
    



     
    
    

 
