from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('room_tariff', room_tariff, name="room_tariff"),
    path('room_detail', room_detail, name="room_detail"),
    path('gallery', gallery, name="gallery"),
    path('save_reservation', save_reservation, name="save_reservation"),
]
