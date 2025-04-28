from django.db import models
from django.contrib.auth.models import User
from roomandsuites.models import Room, Roomtype

# Create your models here.



class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_booked')
    check_in = models.DateField()
    check_out = models.DateField()
    adults = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

class Booking_Query(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_queries')
    room_type = models.ForeignKey(Roomtype, on_delete=models.CASCADE, related_name='roomtype_queries')
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    adults = models.PositiveIntegerField()
    no_of_rooms = models.PositiveIntegerField()
