from django.shortcuts import render
from rest_framework.views import APIView
from .searializers import *
# from .models import *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class RoomType(APIView):
    def post(self, request):
        searilizer = RoomTypeSearilizer(data=request.data)

        if not searilizer.is_valid():
            return Response({'Error': searilizer.errors})
        
        searilizer.save()
        return Response({'Success': 'Room Added successfully'})
    
    def get(self, request):
        room_type = Room_type.objects.all()
        searilizer = RoomTypeSearilizer(room_type, many=True)

        return Response(searilizer.data)
    
class RoomsView(APIView):
    def get(self,request):
        query= Rooms.objects.all()
        serializer = RoomSearilizers(query, many=True)
        
        return Response({'Success': 'Got the Records', 'data': serializer.data})
        
    def post(self, request):
        data = request.data
        serializer = RoomSearilizers(data=data)

        if not serializer.is_valid():
            return Response({'Error': serializer.errors})
        else:
            return Response({'Success': 'Room Added Successfully'})

    def delete(self, request):
        data= request.data.get('id')
        room = Rooms.objects.get(id=data)
        room.delete()
        return Response({'Success': 'Room Deleted Successfully'})
    
    def put(self,request):
        data= request.data.get('id')
        try:
            room = Rooms.objects.get(id=data)
        except:
            return Response('No Rooms found for this id')
        
        serializer = RoomSearilizers(instance=room, data=request.data, partial=True)

        if not serializer.is_valid():
            return Response({'Error': serializer.errors})
        serializer.save()
        return Response({'Success': 'Room Updated Successfully'})
    
class RoomReservation(APIView):
    def post(self, request):
        serializers = ReservationSearilizer(data=request.data)
        if not serializers.is_valid():
            return Response({'Error': serializers.errors})
        
        room_id = serializers.validated_data.get('room_id')
        check_total_room = Rooms.objects.get(id=room_id.id)
        check_room_available = Reservation.objects.filter(room_id=serializers.validated_data.get('room_id'),reservation_date= serializers.validated_data['reservation_date']).count()
        
        if check_total_room.total_rooms > check_room_available:
            serializers.save()
            return Response({'Success': serializers.data})
        else:
            return Response({'Not Available':'Rooms are Not available at this date'})

    def get(self, request):
        reservation = Reservation.objects.all()
        serializers = ReservationSearilizer(reservation, many=True)
        return Response(serializers.data)
        