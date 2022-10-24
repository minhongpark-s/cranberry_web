from django.urls import path, include
from . import views

# for rest Framework tutorial.
from rest_framework import routers
from dashboard.views import RobotDataViewSet
router = routers.DefaultRouter()
router.register('robotData',RobotDataViewSet)
 
urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('topic',views.topicConnectionTest, name ='topicConnectionTest'),
    path('jsonTest',views.jsonTest, name='jsonTest'),
    path('databaseTest', views.databaseTest, name='databaseTest'),
    path('robotDataCleanUp', views.robotDataCleanUp,),
    path('updateDatabase/',views.updateDatabase),
    path('ajax_method/',views.ajax_method, name='ajax_method'),

    # for rest Framework tutorial.
    #path('go/', include(router.urls)),
    path('go/', views.get_api),
]