from django.shortcuts import render


def city_view(request):
    if request.method == 'GET':
        return render(request, template_name='city/gorod.html')



