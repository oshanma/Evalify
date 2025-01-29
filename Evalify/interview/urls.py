from django.urls import path
from .views import home, start_interview , upload_video

urlpatterns = [
    path('', home, name='home'),
    path('start/', start_interview, name='start_interview'),
    path('upload/', upload_video, name='upload_video'),

]
