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


class Storege(ListView):
    model = Store
    template_name = 'storage.html'
    context_object_name = 'store'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items())) 

    def get_success_url(self):
        return reverse_lazy('add')    
        

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
     
      
      
      
      
      
      
      
    
    



     
    
    

 
