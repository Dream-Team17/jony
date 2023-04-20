from django.urls import path
from .views import faculty_five_view

urlpatterns = [
    path('', faculty_five_view)
]

