from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('topic',views.topicConnectionTest, name ='topicConnectionTest'),
    path('jsonTest',views.jsonTest, name='jsonTest'),
    path('databaseTest', views.databaseTest, name='databaseTest'),
    path('updateDatabase',views.updateDatabase),
    path('ajax_method/',views.ajax_method, name='ajax_method'),
]