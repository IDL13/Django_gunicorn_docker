from multiprocessing import AuthenticationError
from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, TextInput

class AuthorizationForm(forms.Form):
    adress = forms.ModelChoiceField(empty_label = 'Выберите здание',queryset = Adress.objects.all(), label = '')
    jobtitle = forms.ModelChoiceField(empty_label = 'Выберете вашу должность', queryset = User.objects.all(), label = '')


class AccountingForm(forms.Form):
    users = forms.CharField(max_length = 30)
    technincs = forms.CharField(max_length = 50)
    create = forms.DateField()
    tecNumber = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AccountingForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Accounting
        fields = ['users', 'technincs', 'create', 'tecNumber']


class StoreForm(forms.Form):
    technincs = forms.CharField(max_length = 50)
    tecNumber = forms.IntegerField()


class AddStorageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = Store
        fields = ['technincs','tecNumber', 'status']

        
class AddAccountingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = Accounting
        fields = ['users','technincs', 'tecNumber']
            

class LoginUserForm(AuthorizationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-input'}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginUserForm, self).__init__(*args, **kwargs)


