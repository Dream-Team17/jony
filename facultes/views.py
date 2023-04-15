from django.shortcuts import render
from django.views.generic import ListView
from .models import Faculty, Comment


def faculties_view(request):
    if request.method == "GET":
        faculties = Faculty.objects.all()

        data = {
            'faculties': faculties
        }
        return render(request, 'facultes/facult1.html', context=data)


def detail_faculty_view(request, id):
    if request.method == 'GET':
        faculty = Faculty.objects.get(id=id)
        comments = Comment.objects.filter(faculty__id=id)

        data = {
            'faculty': faculty,
            'comments': comments
        }

        return render(request, 'facultes/detail.html', context=data)
