from multiprocessing import AuthenticationError
from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, TextInput

class AuthorizationForm(forms.Form):
    adress = forms.ModelChoiceField(empty_label = 'Выберите здание',queryset = Adress.objects.all(), label = '')
    jobtitle = forms.ModelChoiceField(empty_label = 'Выберете вашу должность', queryset = User.objects.all(), label = '')
    login = forms.CharField(max_length = 40,label = 'Логин')
    password = forms.CharField( max_length = 40,label = 'Пароль', widget=forms.PasswordInput())

class AccountingForm(forms.Form):
    users = forms.CharField(max_length = 30)
    technincs = forms.CharField(max_length = 50)
    create = forms.DateField()
    tecNumber = forms.IntegerField()

class StoreForm(forms.Form):
    technincs = forms.CharField(max_length = 50)
    tecNumber = forms.IntegerField()

class AddForm(forms.Form):
    users = forms.CharField(max_length = 30, label="Пользователь")
    technincs = forms.CharField(max_length = 50, label="Техника")
    create = forms.DateField(label="Дата создания")
    tecNumber = forms.IntegerField(label="Техномер")




