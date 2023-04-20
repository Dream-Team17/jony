from django.shortcuts import render
from .models import Group, Announcement

# def board_view(request):
#     if request.method == 'GET':
#         return render(request, template_name='board/doska.html')


def groups_view(request):
    if request.method == 'GET':
        boards = Group.objects.all()

        data = {
            'boards': boards
        }
        return render(request, template_name='board/doska.html', context=data)


def detail_group_view(request, board_id):
    if request.method == 'GET':
        board = Group.objects.get(id=board_id)
        # announcements = Announcement.objects.filter(board__id=board_id)

        data = {
            'board': board,
            # 'announcements': announcements
        }
        return render(request, template_name='board/detail_group.html', context=data)


