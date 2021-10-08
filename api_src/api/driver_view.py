from rest_framework.serializers import Serializer

from . import models, serializers, driver_model
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import permissions, status
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.hashers import check_password

class SignInView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.DriverSignInSerializer
    
    def post(self, request, format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            instanceDriver = driver_model.Driver.objects.filter(username = serializer.validated_data['username'])
            if check_password(serializer.validated_data['password'], instanceDriver[0].password):
                refreshToken = TokenObtainPairSerializer.get_token(instanceDriver[0])
                driverSerializer = serializers.DriverSerializer(instanceDriver[0])
                data = {
                    'refresh_token': str(refreshToken),
                    'access_token': str(refreshToken.access_token),
                    'driver': driverSerializer.data
                }
                print(data)
                return Response(data, status = status.HTTP_200_OK)
            return Response({'error': 'No user found!'}, status = status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Password or email is invalid!'}, status = status.HTTP_400_BAD_REQUEST)
    

class DriverView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.DriverSerializer
    
    def post(self, request, format = None):
        print(request.data)
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
           serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
           serializer.save()
           return Response({'status': 'Created'}, status = status.HTTP_201_CREATED)
        return Response({'error': 'There are some errors! Please try again later!'}, status = status.HTTP_400_BAD_REQUEST)
    
    
class MiddleWare(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format = None):
        return Response('OK', status = status.HTTP_200_OK)