from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView


class IndexView(ListView):
    template_name = 'info/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)