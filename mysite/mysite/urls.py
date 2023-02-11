from django.contrib import admin

from django.urls import *
from school.views import *
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginUser.as_view(), name = 'homepage'),
    path('storege/', Storege.as_view(), name = "storege"),
    path('add/', Add.as_view(),  name = 'add' ),
    path('table/', Table.as_view(), name = 'table')
]