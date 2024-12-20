from django.shortcuts import redirect 
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .serializers import UserSerializer,ProfileSerailizer,RegistrationSerializer
from . models import Profile
from django.contrib.auth.models import User 
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate, login , logout

# registration 
class RegistrationView(APIView):
    def post (self,request):
        if request .user is authenticate:
            pass
        try:
            serializers= RegistrationSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()

                return Response(serializers.data, status =status.HTTP_201_CREATED)
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e :
            return Response({"error":str(e)},status = status .HTTP_500_INTERNAL_SERVER_ERROR)


# Create your views here.

class loginview(APIView):
    permission_class=[IsAuthenticated]
    def post (self ,request):
        try:
            username= request . data.get ("username")
            password= request. data.get("password")
            user= authenticate(username=username,password=password)
            if user is not None :
                login(request,user)
                return Response({"message":"user login successfully"}, status = status . HTTP_200_OK) 
                return Response({"message":"username/password not correct"}, status = status . HTTP_400_BAD_REQUEST) 
        except   Exception as e :
            return Response({'error'}, status = status. HTTP_500_INTERNAL_SERVER_ERROR)


# LOGOUT
class logoutView(APIView):
    def post(self,request):
        try:
            logout(request)
            return Response({"message":"logout Sucessful"},status =status .HTTP_200_OK)
        except Exception as e:
            return Response({'error' : str (e)},status .HTTP_500_INTERNAL_SERVER_ERROR) 
        

# dashboardView ()

class LogoutView (APIView):
    def get(self,request):
        try:
            Profile= request.user.profile
            serializers= UpdateProfileSerializer(profile)
            return Response(serializers.data,status=status.HTTP_200_OK)
        except Exception as e :
            return Response({'error':str(e)}, status = status .HTTP_500_INTERNAL_SERVER_ERROR)


def put(self,request):
    try:
        profile= request.user .profile
        serializer = updateprofileserializer (profile,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as e :
        return Response ({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR) 