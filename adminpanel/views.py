from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.

@login_required
def admin(request):
    user = request.user
    if user.is_staff == True:
        return render(request, 'adminpanel/dashboard.html')
    return HttpResponse('Not allowed 404!')


@login_required
def bookings(request):
    user = request.user
    if user.is_staff == True:
        return render(request, 'adminpanel/bookings.html')
    return HttpResponse('Not allowed 404!')



