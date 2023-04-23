from django.shortcuts import render

def faculty_five_view(request):
    if request.method == 'GET':
        return render(request, template_name='faculty-5/facult5.html')


def history_view(request):
    if request.method == 'GET':
        return render(request, template_name='faculty-5/history.html')


def stengazeta_view(request):
    if request.method == "GET":
        return render(request, template_name='faculty-5/stengazeta.html')