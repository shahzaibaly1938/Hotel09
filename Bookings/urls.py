from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings, name='bookings'),
    path('book-room/', views.book_room, name='book_room'),
    path('check-availbility/', views.check_availbility, name='check_availbility'),
    path('clients_profile/<str:user>/', views.clients_profile, name='clients_profile'),

]