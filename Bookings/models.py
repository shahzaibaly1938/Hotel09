from django.db import models
from django.contrib.auth.models import User
from roomandsuites.models import Room

# Create your models here.



class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_booked')
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)