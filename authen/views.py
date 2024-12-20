from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

# Register Logic Start From Here
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if password != re_password:
            messages.error(request, 'Password Does not match.')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exist.')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exist')
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created Successfully..! Please Login.')
        return redirect('login')
    return render(request, 'authen/register.html')
#Register Logic Ends Here

#Login Logic Start from here
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')
    return render(request, 'authen/login.html')
#Login logic end here

#logout logic
@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')
# logout logic end here


#Showing Profile of User
@login_required
def profile(request):
    return render(request, 'authen/profile.html', {'user': request.user})

