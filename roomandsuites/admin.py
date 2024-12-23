from django.contrib import admin
from .models import Room, Roomtype
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ["name", "is_available", "price", "desc"]

class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Room, RoomAdmin)
admin.site.register(Roomtype, RoomTypeAdmin)