from django.urls import path

from info.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]
