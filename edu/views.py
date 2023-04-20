from django.shortcuts import render


def edu_view(request):
    if request.method == 'GET':
        return render(request, template_name='edu/obrazovanie.html')


def schedule_view(request):
    if request.method == 'GET':
        return render(request, template_name='edu/raspisanie.html')


def lessons_view(request):
    if request.method == 'GET':
        return render(request, template_name='edu/disciplina.html')


def videos_view(request):
    if request.method == 'GET':
        return render(request, template_name='edu/video.html')


def journals_view(request):
    if request.method == 'GET':
        return render(request, template_name='edu/jurnal.html')


def library_view(request):
    if request.method == 'GET':
        return render(request, template_name='edu/Biblioteka.html')
