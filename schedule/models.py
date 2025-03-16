from django.db import models
from users.models import CustomUser

# Create your models here.

class event(models.Model):

    name = models.CharField(max_length=30)

class presence(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(event, on_delete = models.DO_NOTHING)
    startdate = models.DateField()
    enddate = models.DateField()