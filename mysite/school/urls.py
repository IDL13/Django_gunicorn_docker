from distutils.command.build import build
from django.urls import path
from .views import *


urlpatterns = [
       path ('accounting',Add_accounting.as_view(), name = 'add_accounting'),
       path ('delete/<int:tec>/', Table.delete),
       path('update/<int:tec>', Table.update),
]