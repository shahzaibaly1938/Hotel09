from django.urls import path
from . import views

urlpatterns = [
    path('our_rooms/', views.roomsandsuites, name='roomsandsuites'),
    path('', views.rooms, name='rooms'),
    path('create_room/', views.create_room, name='create_room'),
    path('create_roomtype', views.create_roomtype, name='create_roomtype')
]