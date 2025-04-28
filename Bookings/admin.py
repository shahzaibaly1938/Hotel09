from django.contrib import admin
from .models import Booking , Booking_Query

# Register your models here.



class BookingAdmin(admin.ModelAdmin):
    list_display = ["room", "user", "check_in", "check_out", "created_at"]

class Booking_Query_Admin(admin.ModelAdmin):
    list_display = ["room_type", "user", "check_in", "check_out", "no_of_rooms", "adults", "created_at"]



admin.site.register(Booking, BookingAdmin)
admin.site.register(Booking_Query, Booking_Query_Admin)
