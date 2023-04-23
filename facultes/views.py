from django.shortcuts import render

from .models import Faculty, Comment
from users.utils import get_user_from_request


def faculties_view(request):
    if request.method == "GET":
        faculties = Faculty.objects.all()

        data = {
            'faculties': faculties,
            'user':get_user_from_request(request)
        }
        return render(request, 'facultes/svedenia.html', context=data)


def detail_faculty_view(request, faculty_id):
    if request.method == 'GET':
        faculty = Faculty.objects.get(id=faculty_id)
        # comments = Comment.objects.filter(faculty__id=faculty_id)

        data = {
            'faculty': faculty,
            'user': get_user_from_request(request)
            # 'comments': comments
        }

        return render(request, 'facultes/detail.html', context=data)
