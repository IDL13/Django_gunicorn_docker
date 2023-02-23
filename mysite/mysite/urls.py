from django.contrib import admin

from django.urls import *
from school.views import *
from school import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginUser.as_view(), name = 'homepage'),
    ########################################################
    path('storage/', Storage.as_view(), name = "storage"),
    path('storage/add_storage',Add_storage.as_view(), name = 'add_storage'),
    path("storage/delete/<int:tec>", Storage.delete, name = 'delete_storage'),
    path("storage/update/<int:tec>", Storage.update, name = 'update_storage'),
    ########################################################
    path('add/', include("school.urls")),
    path('table/', Table.as_view(), name = 'table'),
    path("table/", include("school.urls")),
]