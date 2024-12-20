from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.admin, name='admin'),
    path('bookings/', views.bookings, name='bookings'),
    path('rooms/', include("roomandsuites.urls")),
]