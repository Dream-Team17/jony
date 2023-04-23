from django.shortcuts import render
from .models import Country
from users.utils import get_user_from_request


def country_view(request):
    if request.method == 'GET':
        countries = Country.objects.all()

        data = {
            'countries': countries,
            'user': get_user_from_request(request)
        }

        return render(request, template_name='countries/country.html', context=data)


def detail_country_view(request, country_id):
    if request.method == 'GET':
        country = Country.objects.get(id=country_id)

        data = {
            'country': country,
            'user': get_user_from_request(request)
        }

        return render(request, template_name='countries/detail.html', context=data)
