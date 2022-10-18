from statistics import mode
from django.db import models

# Create your models here.

class Question(models.Model):
    title=models.TextField()

class RobotPosition(models.Model):
    Robotposition=models.IntegerField()
    connectionStatus=models.TextField()

'''
class Version(models.Model):
    version = models.CharField(max_length=10)

    def __str__(self):
        return self.version
'''