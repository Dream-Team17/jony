from django.urls import path
from .views import groups_view, detail_group_view

urlpatterns = [
    path('', groups_view),
    path('<int:grups_id>/', detail_group_view)
]

