from django.shortcuts import render
from .models import CustomUser
from alert.models import Notification
from rest_framework import generics,status,permissions,viewsets
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import LoginSerializer,SignUpSerializer,ProfileSerializer
from django.contrib.contenttypes.models import ContentType
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
    
class ProfileView(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        #return super().update(request, *args, **kwargs)
        user=self.request.user
        profile=self.get_object()

        if request.user.username!=profile.username:
            return Response(
                {"message":"You can't edit someone else's profile!"},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().update(request, *args, **kwargs)


class FollowView(generics.GenericAPIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,pk):
        profile=generics.get_object_or_404(CustomUser,pk=pk)
        user=request.user

        if profile==user:
            return Response({
                "error":"You can't follow your self"
                },status=status.HTTP_403_FORBIDDEN)
        else:
            user.following.add(profile)
            Notification.objects.create(
                recipient=profile,
                actor=user,
                verb=f"{profile.username} followed you!",
                content_type=ContentType.objects.get_for_model(CustomUser),
                object_id=profile.id
            )
            return Response(
                    {"message": f"You are now following {profile.username}"},
                    status=status.HTTP_201_CREATED
                    )
    
class UnfollowView(generics.GenericAPIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,pk):
        profile=generics.get_object_or_404(CustomUser,pk=pk)
        user=request.user

        if profile==user:
            return Response({
                "error":"You can't unfollow your self"
                },status=status.HTTP_403_FORBIDDEN)
        else:
            user.following.remove(profile)
            
            return Response(
                    {"message": f"You unfollowed {profile.username}"},
                    status=status.HTTP_200_OK
                )