from django.shortcuts import render
from users.utils import get_user_from_request


def city_view(request):
    if request.method == 'GET':
        data = {
            'user': get_user_from_request(request)
        }
        return render(request, template_name='city/gorod.html', context=data)



