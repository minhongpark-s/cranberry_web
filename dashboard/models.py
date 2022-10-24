from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
    	db_table = 'menu'

class robotData(models.Model):
    checked_at = models.DateTimeField(auto_now_add=True)
    robotPositionX = models.IntegerField()
    robotPositionY = models.IntegerField()
    
