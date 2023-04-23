from django.urls import path
from .views import faculty_five_view, history_view, stengazeta_view

urlpatterns = [
    path('', faculty_five_view),
    path('history/', history_view),
    path('stengazeta/', stengazeta_view)
]

