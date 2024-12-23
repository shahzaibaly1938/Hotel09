from django.contrib import admin
from .models import Booking

# Register your models here.



class BookingAdmin(admin.ModelAdmin):
    list_display = ["room", "user", "check_in", "check_out", "created_at"]



admin.site.register(Booking, BookingAdmin)
