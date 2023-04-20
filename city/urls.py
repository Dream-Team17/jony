from django.urls import path
from .views import city_view

urlpatterns = [
    path('', city_view)
]
