from django.db import models

# Create your models here.

class Roomtype(models.Model):
    name = models.CharField(max_length=100)
    

class Room(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Roomtype, on_delete=models.CASCADE, related_name='roomtype_rooms')
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image1_main = models.ImageField(upload_to='room_images/')
    image2 = models.ImageField(upload_to='room_images/')
    image3 = models.ImageField(upload_to='room_images/')
    image360 = models.ImageField(upload_to='room_images/')



