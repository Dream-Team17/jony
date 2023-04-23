from django.shortcuts import render
from users.utils import get_user_from_request

def edu_view(request):
    if request.method == 'GET':
        data = {
            'user': get_user_from_request(request)
        }
        return render(request, template_name='edu/obrazovanie.html', context=data)


def schedule_view(request):
    if request.method == 'GET':
        data = {
            'user': get_user_from_request(request)
        }
        return render(request, template_name='edu/raspisanie.html', context=data)


def lessons_view(request):
    if request.method == 'GET':
        data = {
            'user': get_user_from_request(request)
        }
        return render(request, template_name='edu/disciplina.html', context=data)


def videos_view(request):
    if request.method == 'GET':
        data = {
            'user': get_user_from_request(request)
        }
        return render(request, template_name='edu/video.html', context=data)


def journals_view(request):
    if request.method == 'GET':
        data = {
            'user': get_user_from_request(request)
        }
        return render(request, template_name='edu/jurnal.html', context=data)


def library_view(request):
    if request.method == 'GET':
        data = {
            'user': get_user_from_request(request)
        }
        return render(request, template_name='edu/Biblioteka.html', context=data)
