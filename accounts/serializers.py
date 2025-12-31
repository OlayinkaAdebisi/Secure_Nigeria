from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
#from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

User=get_user_model()
class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model=CustomUser
        fields = ['id', 'first_name','last_name', 'username', 'email', 'password']

    def create(self,validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            username=attrs.get('username'),
            password=attrs.get('password')
        )

        if not user:
            raise serializers.ValidationError("invalid")
        
        return {'user': user}
    
class ProfileSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    followings = serializers.SerializerMethodField()

    class Meta:
        model=CustomUser
        fields=['id', 'username', 'first_name', 'last_name', 'date_of_birth', 'phone_number', 'followers', 'followings','profile_picture']
        read_only_fields = ['username', 'followers', 'followings']

    def get_followers(self,obj):
        return obj.followers.count()
    
    def get_followings(self,obj):
        return obj.following.count()
    