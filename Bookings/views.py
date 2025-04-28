from django.shortcuts import render, redirect
from .models import Booking, Booking_Query
# from roomandsuites import Room
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from roomandsuites.models import Roomtype
from django.contrib.auth.models import User

# Create your views here.

# def book_room(request, room_id):
#     room = Room.objects.get(id=room_id)
#     if request.method == 'POST':
#         check_in = request.POST['check_in']
#         check_out = request.POST['check_out']
#         Booking.objects.create(user=request.user, room=room, check_in=check_in, check_out=check_out)
#         return redirect('booking-success')
#     return render(request, 'Bookings/bookroom.html', {'room':room})

@login_required
def bookings(request):
    user = request.user
    if user.is_staff == True:
        queries = Booking_Query.objects.all()
        return render(request, 'Bookings/bookings.html',{'queries':queries})

@login_required
def book_room(request):
    room_type = Roomtype.objects.all()
    return render(request, 'Bookings/bookroom.html',{'room_type':room_type})

@login_required
def check_availbility(request):
    user = request.user
    if request.method == 'POST':
        room_type = request.POST['room_type']
        checkin = request.POST['checkin']
        checkout = request.POST['checkout']
        adults = request.POST['adults']
        no_of_rooms = request.POST['no_of_rooms']
        Booking_Query.objects.create(user=user, room_type=Roomtype.objects.get(name=room_type), check_in=checkin, check_out=checkout, adults=adults, no_of_rooms=no_of_rooms)
    messages.success(request, "Query Submit Sucessfully we'll contact you in short..")
    return redirect('roomsandsuites')

@login_required
def clients_profile(request, user):
    print(user)
    client = User.objects.get(username=user)
    print(client)
    return render(request, 'Bookings/clients_profile.html', {'client':client})