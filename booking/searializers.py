from rest_framework import serializers
from .models import *

class RoomTypeSearilizer(serializers.ModelSerializer):
    class Meta:
        model = Room_type
        fields = '__all__'

class RoomSearilizers(serializers.ModelSerializer):
    # type = RoomTypeSearilizer()
    class Meta:
        model = Rooms
        exclude = ['photos']

class ReservationSearilizer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

