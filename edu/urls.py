from django.urls import path
from .views import edu_view, schedule_view, lessons_view, videos_view, journals_view, library_view

urlpatterns = [
    path('', edu_view),
    path('schedule/', schedule_view),
    path('lessons/', lessons_view),
    path('videos/', videos_view),
    path('journals/', journals_view),
    path('library/', library_view),
]
