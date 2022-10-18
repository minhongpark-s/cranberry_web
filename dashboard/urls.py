from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('topic',views.topicConnectionTest, name ='topicConnectionTest'),
]