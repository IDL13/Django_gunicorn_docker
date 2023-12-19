from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import re_path

from django.urls import *
from school.views import *

#startp paths
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FirsPage.observe, name = 'homepage'),
    path('login', LoginUser.as_view(), name = 'login'),
    path('login/', include('school.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
