from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.admin, name='admin'),
    path('rooms/', include("roomandsuites.urls")),
    path('bookings/', include("Bookings.urls")),
]