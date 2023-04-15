from django.urls import path
from .views import country_view, detail_country_view

urlpatterns = [
    path('', country_view),
    path('<int:country_id>/', detail_country_view)
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
