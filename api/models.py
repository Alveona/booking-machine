from django.db import models
from django.conf import settings

# Create your models here.

class Room(models.Model):
    number = models.IntegerField()
    desc = models.CharField(max_length = 255)

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null = True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null = True)
    time_from = models.DateTimeField()
    time_until = models.DateTimeField()
