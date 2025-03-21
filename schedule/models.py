from django.db import models
from users.models import CustomUser

# Create your models here.

class Event(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Visit(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete = models.DO_NOTHING)
    startdate = models.DateField()
    enddate = models.DateField()