from django.urls import path

from .views import faculties_view, detail_faculty_view

urlpatterns = [
    path('', faculties_view),
    path('<int:faculty_id>/', detail_faculty_view)
]