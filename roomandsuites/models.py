from django.db import models

# Create your models here.

class Roomtype(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Room(models.Model):
    id = models.IntegerField(primary_key= True, default=None)
    name = models.CharField(max_length=100)
    room_type = models.ForeignKey(Roomtype, on_delete=models.CASCADE, related_name='roomtype_rooms')
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image1_main = models.ImageField(upload_to='static/room_images/')
    image2 = models.ImageField(upload_to='static/room_images/')
    image3 = models.ImageField(upload_to='static/room_images/')
    image360 = models.ImageField(upload_to='static/room_images/')

    def __str__(self):
        return f"{self.name} : {self.price}" 



