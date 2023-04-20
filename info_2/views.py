from django.shortcuts import render

from .models import MainImage_2


# Create your views here.
def index_view(request):
    if request.method == 'GET':
        return render(request, template_name='layouts/index.html')


def main_image_view(request):
    if request.method == 'GET':
        images = MainImage_2.objects.all()
        data = {
            'images': images
        }

        return render(request, template_name='info/main_page.html', context=data)
