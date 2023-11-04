from distutils.command.build import build
from django.urls import path
from school.views import *

urlpatterns = [
       # main table urls
       path("table/", Table.as_view(), name = "table"),
       path ("table/accounting",Add_accounting.as_view(), name = "add_accounting"),
       path ("table/delete/<int:id>/", Table.delete),
       path("table/update/<int:id>", Table.update),
       path("table/find/",Table.find, name = "find"),
       path("table/save-in-xml", Upload.save_in_xml ,name = "save_in_xml"),
       path("table/read_from_xml", Upload.all_xml, name = "all_xml"),
       path("table/read_from_xml/<str:file>",Upload.read_from_xml, name = "read_from_xml" ),
       
       
       # storage urls
       path("storage/<int:count>", Storage.get_objects, name = "storage"),
       path("storage/50", Storage.get_objects, name = "stor"),
       path("storage/add_storage",Add_storage.as_view(), name = "add_storage"),
       path("storage/delete/<int:id>", Storage.delete, name = "delete_storage"),
       path("storage/update/<int:id>", Storage.update, name = "update_storage"),
       path("storage/qr/<int:id>", Storage.qr, name = "qr"),
       path("storage/find/",Storage.find, name = "find_storage"),
       path("storage/drop_db", Storage.drop, name = "drop"),
       

       #upload urls
       path("upload/", Upload.simple_upload, name = "upload"),
]
