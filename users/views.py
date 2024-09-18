from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .searializers import *
from rest_framework.response import Response
from .models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
#Create your views here.

class Register(viewsets.ViewSet):
    def create(self, request):
        data= request.data
        serializers = RegisterSearilizers(data=data)

        if not serializers.is_valid():
            return Response({'Error': serializers.errors})
        
        serializers.save()
        return Response({'data': serializers.data})
    
    def list(self, request):
        queryset = CustomUser.objects.all()
        serializers = RegisterSearilizers(queryset, many=True)

        return Response({'data': serializers.data})
    
class Login(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'error': serializer.errors})

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = authenticate(request, username=username, password=password)
        refresh = RefreshToken.for_user(user)
        if user is not None:
            return Response({'message': 'Successfully logged in', 'refresh': str(refresh),
        'access': str(refresh.access_token)})
        else:
            return Response({'error': 'Invalid username or password'})