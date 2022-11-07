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

        user = authenticate(request, login=log, password=pas)
        login(request, user)
        if adres == "1" and job == "1":
            request.session.set_expiry(500)
            request.session['pause'] = True
            return render(request, 'school/Okt_zavh.html', {'acounting': acounting, 'store': store})
        elif adres == "1" and job == "2":
            request.session.set_expiry(500)
            request.session['pause'] = True
            return render(request, 'school/Okt_admin.html', {'acounting': acounting, 'store': store})
        elif adres == "1" and job == "3":
            request.session.set_expiry(500)
            request.session['pause'] = True
            return render(request, 'school/Okt_HDR.html', {'acounting': acounting, 'store': store})
        
def storege (request):
    if request.method == 'GET':
        store = StoreForm()
        store = Store.objects.all()
        request.session.set_expiry(500)
        request.session['pause'] = True
        return render(request, 'storege.html', {'store': store})
    else:
        return redirect('/')

def add(request):
    if request.method == "GET":
        add_inf = AddForm()
        request.session.set_expiry(500)
        request.session['pause'] = True
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


      
      
      
      
      
      
      
      
    
    



     
    
    

 
