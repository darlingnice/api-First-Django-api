from django.db import models 

class UserData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    state = models.CharField(max_length=100)
    