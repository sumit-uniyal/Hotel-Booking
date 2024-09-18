from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.conf import settings

# router = DefaultRouter()
# router.register(r'rooms', RoomsView, basename='rooms')

urlpatterns = [
    # path('', include(router.urls)),
    path('room/', RoomsView.as_view(),  name="room"),
    path('room_type', RoomType.as_view(),  name="room_type"),
    path('room_reservation/', RoomReservation.as_view(),  name="room_reservation")
]