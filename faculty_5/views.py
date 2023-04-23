from django.shortcuts import render
from users.utils import get_user_from_request

def faculty_five_view(request):
    if request.method == 'GET':
        data = {
            'user': get_user_from_request(request)
        }
        return render(request, template_name='faculty-5/facult5.html', context=data)


def history_view(request):
    if request.method == 'GET':
        data = {
            'user': get_user_from_request(request)
        }
        return render(request, template_name='faculty-5/history.html', context=data)


def stengazeta_view(request):
    if request.method == "GET":
        data = {
            'user': get_user_from_request(request)
        }
        return render(request, template_name='faculty-5/stengazeta.html', context=data)

