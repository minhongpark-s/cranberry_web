from .base import * #base.py 파일의 모든 내용을 사용

ALLOWED_HOSTS = [] #ALLOWED_HOSTS만 다르게 설정

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'check_db',
        'USER' : 'root', 
        'PASSWORD' : '123456789',
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}