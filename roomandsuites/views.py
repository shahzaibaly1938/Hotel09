from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Room
from django.contrib import messages

# Create your views here.


@login_required
def rooms(request):
    user = request.user
    if user.is_staff == True:
        rooms = Room.objects.all()
        print(rooms)
        return render(request, 'roomandsuites/rooms.html', {'rooms':rooms})
    return HttpResponse('Not allowed 404!')

@login_required
def create_room(request):
    user = request.user
    if user.is_staff == True:
        if request.method == 'POST':
            name = request.POST['name']
            price  = request.POST['price']
            is_available = request.POST.get('is_available')
            image1 = request.FILES.get('room_image1')
            image2 = request.FILES.get('room_image2')
            image3 = request.FILES.get('room_image3')
            image360 = request.FILES.get('360_image')
            desc = request.POST['desc']
            if is_available == 'on':
                is_available = True
            elif is_available is None:
                is_available = False

            Room.objects.create(name=name, price=price, is_available=is_available, image1_main=image1, image2=image2, image3=image3, image360=image360, desc=desc)
            messages.success(request, "Room Created Sucessfully..")
            return redirect('rooms')
            
        return render(request, 'roomandsuites/create_rooms.html')
    return HttpResponse('Not allowed 404!')