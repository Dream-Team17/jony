from django.urls import path
from .views import index_view, main_image_view

urlpatterns = [
    path('navbar/', index_view),
    path('', main_image_view)
]