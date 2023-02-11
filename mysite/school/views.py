from operator import getitem
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView, DeleteView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout, authenticate


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main_page.html'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('table')

class Table(ListView):
    model = Accounting
    template_name = 'build.html'
    context_object_name = 'acounting'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items())) 

    def get_success_url(self):
        return reverse_lazy('add') 


# def input(request):
#     if request.method == 'GET':
#         form = AuthorizationForm()
#         return render(request, 'base.html', {'form': form})
#     else:
#         adres = request.POST.get('adress')
#         job = request.POST.get('jobtitle')
#         log = request.POST.get('login')
#         pas = request.POST.get('password')

#         acounting = Accounting.objects.all()
#         store = Store.objects.all()

#         acounting = Accounting.objects.all()
#         store = Store.objects.all()

#         user = authenticate(request, login=log, password=pas)
#         login(request, user)
#         if adres == "1" and job == "1":
#             return render(request, 'school/Okt_zavh.html', {'acounting': acounting, 'store': store})
#         elif adres == "1" and job == "2":
#             return render(request, 'school/Okt_admin.html', {'acounting': acounting, 'store': store})
#         elif adres == "1" and job == "3":
#             return render(request, 'school/Okt_HDR.html', {'acounting': acounting, 'store': store})

class Storege(ListView):
    model = Store
    template_name = 'storege.html'
    context_object_name = 'store'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items())) 

    def get_success_url(self):
        return reverse_lazy('add')    
        
# def storege (request):
#     if request.method == 'GET':
#         store = StoreForm()
#         store = Store.objects.all()
#         return render(request, 'storege.html', {'store': store})
#     else:
#         return redirect('/')

class Add(CreateView):
    form_class =  AddForm
    template_name = 'add.html'
    context_object_name = 'add'
    success_url = reverse_lazy('homepage')
    # login_url = reverse_lazy('homepage')
    # raise_exception = True

    # def get_context_data(self, *, object_list = None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return dict(list(context.items())) 


    # def get_queryset(self):
    #      return Accounting.objects.all()

# def add(request):
#     if request.method == "GET":
#         add_inf = AddForm()
#         return render(request, 'add.html', {"add": add_inf,} )
#     if request.method == "POST":
#         form = AddForm(request.POST)
#         if form.is_valid():
#             add = Accounting(
#                 users = form.cleaned_data['users'],
#                 technincs = form.cleaned_data['technincs'], 
#                 create = form.cleaned_data['create'],
#                 tecNumber = form.cleaned_data['tecNumber']
#             )
#             add.save()
#             return redirect('/')


      
      
      
      
      
      
      
      
    
    



     
    
    

 
