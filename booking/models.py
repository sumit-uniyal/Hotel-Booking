from django.db import models
from users.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from .mail import send_email_notification

# Create your models here.
class Room_type(models.Model):
    type = models.CharField(max_length=100)

class Rooms(models.Model):
    type = models.ForeignKey(Room_type, on_delete=models.CASCADE)
    prince = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    total_rooms = models.IntegerField()
    photos = models.ImageField(upload_to='rooms')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Reservation(models.Model):
    userName = models.CharField(max_length=100)
    email = models.EmailField(null=False, blank=False)
    phone_no = models.CharField(max_length=50, null=True, blank=True)
    room_id = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    reservation_date = models.DateField()
    message = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.room_id)