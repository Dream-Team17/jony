from django.urls import path
from countries.views import KazakhView, ArmeniaView, BelarusView, KyrgyzstanView, TadjikistanView, UzbekistanView, \
    VietnamView

urlpatterns = [
    path('kazakh/', KazakhView.as_view()),
    path('armenia/', ArmeniaView.as_view()),
    path('belarus/', BelarusView.as_view()),
    path('kyrgyzstan/', KyrgyzstanView.as_view()),
    path('tadjikistan/', TadjikistanView.as_view()),
    path('uzbekistan/', UzbekistanView.as_view()),
    path('vietnam/', VietnamView.as_view()),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
