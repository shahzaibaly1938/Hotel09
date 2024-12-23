from django.shortcuts import render, redirect
from .models import Booking
from roomandsuites import Room

# Create your views here.

def book_room(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        Booking.objects.create(user=request.user, room=room, check_in=check_in, check_out=check_out)
        return redirect('booking-success')
    return render(request, 'booking/book_room.html', {'room':room})

