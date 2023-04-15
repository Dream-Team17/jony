from django.shortcuts import render
from django.views.generic import ListView


class KazakhView(ListView):
    template_name = 'countries/kazah.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ArmeniaView(ListView):
    template_name = 'countries/armenia.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class BelarusView(ListView):
    template_name = 'countries/belarus.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class KyrgyzstanView(ListView):
    template_name = 'countries/kyrgyz.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class TadjikistanView(ListView):
    template_name = 'countries/tadjikistan.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class UzbekistanView(ListView):
    template_name = 'countries/uzbek.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class VietnamView(ListView):
    template_name = 'countries/vietnam.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
