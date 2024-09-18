from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import *

class RegisterSearilizers(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    # text_password = serializers.CharField()

    def validate(self, data):
        if CustomUser.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError('user already exist')
        return data
    
    def create(self, validated_data):
        text_password = validated_data['password']
        user = CustomUser.objects.create(
            username= validated_data['username'],
            email = validated_data['email'],
            text_password= text_password
            )
        user.set_password(validated_data['password'])
        user.save()
        return {
            'username': user.username,
            'email': user.email,
            'password':user.text_password,
        }
    
    def to_representation(self, instance):
        return{
            'id': instance.id,
            'username': instance.username,
            'email': instance.email,
            'password':instance.text_password,
        }
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if not CustomUser.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError('Username not found')
        return data