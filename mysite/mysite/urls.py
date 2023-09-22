from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import *
from school.views import *
from django.views.generic import RedirectView

#startp paths
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FirsPage.observe, name = 'homepage'),
    path('login', LoginUser.as_view(), name = 'login'),
    path('login/', include('school.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
