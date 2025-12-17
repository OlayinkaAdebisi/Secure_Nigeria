from django.shortcuts import render
from .models import Location
from rest_framework import viewsets, permissions
from .serializers import LocationSerializer

# Create your views here.

class LocationViewSet(viewsets.ModelViewSet):
    queryset=Location.objects.all()
    serializer_class=LocationSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)