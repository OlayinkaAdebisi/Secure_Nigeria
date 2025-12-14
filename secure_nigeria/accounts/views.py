from django.shortcuts import render
from .models import CustomUser
from rest_framework import generics,status,permissions
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import LoginSerializer,SignUpSerializer
# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class=SignUpSerializer
    permission_classes=[AllowAny]

    def post(self,request):
        input=self.get_serializer(data=request.data)
        input.is_valid(raise_exception=True)
        user=input.save()
        token, created=Token.objects.get_or_create(user=user)
        return Response({"Token": token.key})
    
class LoginView(generics.GenericAPIView):
    serializer_class=LoginSerializer
    permission_classes=[AllowAny]

    def post(self,request):
        Userinput=self.get_serializer(data=request.data)
        Userinput.is_valid(raise_exception=True)
        user=Userinput.validated_data['user']
        token,created=Token.objects.get_or_create(user=user)
        return Response({"token": token.key})