from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings, name='bookings'),
    path('book-room/', views.book_room, name='book_room')
]