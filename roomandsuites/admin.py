from django.contrib import admin
from .models import Room
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ["name", "is_available", "price", "desc"]


admin.site.register(Room, RoomAdmin)