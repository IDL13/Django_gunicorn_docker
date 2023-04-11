from distutils.command.build import build
from django.urls import path
from school.views import *

urlpatterns = [
       path('storage/', Storage.as_view(), name = "storage"),
       path('storage/add_storage',Add_storage.as_view(), name = 'add_storage'),
       path('storage/delete/<int:tec>', Storage.delete, name = 'delete_storage'),
       path('storage/update/<int:tec>', Storage.update, name = 'update_storage'),
       
       path('table/', Table.as_view(), name = 'table'),
       path ('table/accounting',Add_accounting.as_view(), name = 'add_accounting'),
       path ('table/delete/<int:tec>/', Table.delete),
       path('table/update/<int:tec>', Table.update),
       path('table/find/',Table.find, name = 'find'),
       path('storage/find/',Storage.find, name = 'find_storage'),
       
       path('table/save-in-xml',Table.save_in_xml ,name = "save_in_xml"),
       path('upload/',Table.simple_upload, name = "upload"),
]
