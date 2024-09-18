from django.shortcuts import render
from booking.models import Room_type
from django.http import HttpResponse
import requests
import json
# Create your views here.

def home(request):
    room_data = Room_type.objects.all()
    return render(request, 'frontend/home.html', context={'room_type': room_data})

def room_tariff(request):
    room_data = Room_type.objects.all()
    return render(request, 'frontend/room-tariff.html', context={'room_type': room_data})

def room_detail(request):
    return render(request, 'frontend/room-detail.html')

def gallery(request):
    return render(request, 'frontend/gallery.html')

def save_reservation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        room_type = request.POST.get('room_type')
        reservation_date = request.POST.get('r_date')
        message = request.POST.get('message')
   
        url = "http://127.0.0.1:8000/booking/room_reservation/"

        payload = json.dumps({
        "userName": name,
        "email": email,
        "status": "completed",
        "reservation_date": reservation_date,
        "room_id": room_type
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
 
        
        if 'Success' in response.text:
            message = 'Booking Successfully Completed'
        elif 'Not Available' in response.text:
            message = 'Rooms not Available at this date'
        else:
            message = 'Booking can not be completed at this moment'

        room_data = Room_type.objects.all()
        return render(request, 'frontend/home.html', context={'room_type': room_data, message: message})
    
