from django.contrib import admin

from django.urls import *
from school.views import *
from school import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginUser.as_view(), name = 'homepage'),
    path('storage/', Storege.as_view(), name = "storage"),
    path('add/', include("school.urls")),
    path('table/', Table.as_view(), name = 'table'),
    path("table/", include("school.urls")),
]