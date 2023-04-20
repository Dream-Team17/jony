from django.contrib import admin
from django.urls import path, include

from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info_2.urls')),
    path('countries/', include('countries.urls')),
    path('users/', include('users.urls')),
    path('faculties/', include('facultes.urls')),
    path('edu/', include('edu.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
