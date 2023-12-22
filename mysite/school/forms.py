from multiprocessing import AuthenticationError
from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, TextInput


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
    time = forms.CharField(max_length = 50)


class AddStorageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
    class Meta:
        model = SVT
        fields = ['name','acounting','inv_number','ser_number', 'cmo', 'data_get', 'data_inp', 'quantity']

      
class AddAccountingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
    class Meta:
        model = Accounting
        fields = ['users','technincs', 'tecNumber']
 
     
class AddFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
    class Meta:
        model = File
        fields = ['title','file']              




