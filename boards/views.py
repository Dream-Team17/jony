from django.shortcuts import render, redirect

from django.shortcuts import render
from .models import Group, Announcement
from .forms import AnnouncementCreateForm, GroupCreateForm
from users.utils import get_user_from_request



def groups_view(request):
    if request.method == 'GET':
        boards = Group.objects.all()

        data = {
            'boards': boards,
            'form': GroupCreateForm,
            'user': get_user_from_request(request)

        }
        return render(request, template_name='board/doska.html', context=data)

    if request.method == 'POST':
        form = GroupCreateForm(data=request.POST)

        if form.is_valid():
            Group.objects.create(
                author_id=1,
                title=form.cleaned_data.get('title')
            )
            return redirect('/boards/')
        else:
            boards = Group.objects.all()

            data = {
                'boards': boards,
                'form': form,
                'user': get_user_from_request(request)

            }
            return render(request, template_name='board/doska.html', context=data)

def detail_group_view(request, grups_id):
    if request.method == 'GET':
        gruppa = Group.objects.get(id=grups_id)
        announcements = Announcement.objects.filter(groups__id=grups_id)

        data = {
            'gruppa': gruppa,
            'announcements': announcements,
            'form': AnnouncementCreateForm,
            'user': get_user_from_request(request)

        }
        return render(request, template_name='board/detail_group.html', context=data)

    if request.method == 'POST':

        form = AnnouncementCreateForm(data=request.POST)

        if form.is_valid():

            Announcement.objects.create(
                author_id=1,
                text=form.cleaned_data.get('text'),
                groups_id=grups_id
                )


            return redirect(f'/boards/{grups_id}/')
        else:
            gruppa = Group.objects.get(id=grups_id)
            announcements = Announcement.objects.filter(groups__id=grups_id)

            data = {
                'gruppa': gruppa,
                'announcements': announcements,
                'form': form,
                'user': get_user_from_request(request)

            }
            return render(request, template_name='board/detail_group.html', context=data)



