from .base import *

ALLOWED_HOSTS = ['101.101.217.11'] #서버의 고정 아이피를 등록

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'captin_project',
        'USER' : 'root', 
        'PASSWORD' : 'Bruce1928@park',
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}