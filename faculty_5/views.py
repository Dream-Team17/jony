from django.shortcuts import render

def faculty_five_view(request):
    if request.method == 'GET':
        return render(request, template_name='faculty-5/facult5.html')



