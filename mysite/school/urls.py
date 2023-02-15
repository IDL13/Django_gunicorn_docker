from distutils.command.build import build
from django.urls import path
from .views import *


urlpatterns = [
       path('storage',Add_storage.as_view(), name = 'add_storage'),
       path ('accounting',Add_accounting.as_view(), name = 'add_accounting'),
       path ('delete/<int:tec>/', Table.delete)
]