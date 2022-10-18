from zlib import decompressobj


from django.urls import path
from . import views

urlpatterns = [
    path('',views.QuestionDetail.as_view()), # https://coshin.tistory.com/m/13
    path('robot', views.RobotPositionRequest.as_view())
]