from django.shortcuts import render
from rest_framework import generics
from .serializers import MyUserserializer
from .models import MyUser
# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserserializer
    #permission_classes = [AllowAny]