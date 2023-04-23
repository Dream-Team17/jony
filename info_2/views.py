from django.shortcuts import render
from users.utils import get_user_from_request
from .models import MainImage_2


# Create your views here.
def index_view(request):
    if request.method == 'GET':
        data = {
            'user': get_user_from_request(request)
        }
        return render(request, template_name='layouts/index.html', context=data)


def main_image_view(request):
    if request.method == 'GET':
        images = MainImage_2.objects.all()
        data = {
            'images': images,
            'user': get_user_from_request(request)
        }

        return render(request, template_name='info/main_page.html', context=data)
