from django.shortcuts import render

from django.shortcuts import render
from .models import Group, Announcement




def groups_view(request):
    if request.method == 'GET':
        boards = Group.objects.all()

        data = {
            'boards': boards
        }
        return render(request, template_name='board/doska.html', context=data)


def detail_group_view(request, grups_id):
    if request.method == 'GET':
        gruppa = Group.objects.get(id=grups_id)
        announcements = Announcement.objects.filter(groups__id=grups_id)

        data = {
            'gruppa': gruppa,
            'announcements': announcements
        }
        return render(request, template_name='board/detail_group.html', context=data)

