from django.shortcuts import render
from .models import Location,Stations
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .serializers import LocationSerializer,StationSerializer
import math
# Create your views here.

def distance_approx(lat1,lon1,lat2,lon2):
# Haversine formula
    R = 6371 #radius of earth (km)
# to radian
    la1=(lat1*math.pi)/180
    la2=(lat2*math.pi)/180
    lo1=(lon1*math.pi)/180
    lo2=(lon2*math.pi)/180
# difference between point 1 and 2
    lat=la2-la1
    lon=lo2-lo1
# a = sin²(Δφ/2) + cos(φ₁) * cos(φ₂) * sin²(Δλ/2)
    a = (math.sin(lat/2) ** 2) + math.cos(la1) * (math.cos(la2) * math.sin(lon/2)**2)
#c = 2 * atan2(√a, √(1-a)) or c = 2 * asin(√a)
    c = 2 * math.atan2((math.sqrt(a)), (math.sqrt(1-a)))

    d = R * c
    return d


class LocationViewSet(viewsets.ModelViewSet):
    queryset=Location.objects.all()
    serializer_class=LocationSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)

    @action(detail=False, methods=['get'])
    def nearest_station(self,request):
        user_lat = request.query_params.get('latitude')
        user_log = request.query_params.get('longitude')

        try:
            lat=float(user_lat)
            log=float(user_log)
        except ValueError:
            return Response({"error": "Please input decimal numbers only"},status=400)
        i=float('inf')
        closest_station = None
        for station in Stations:
            dblat=float(station.latitude)
            dblog=float(station.longitude)
            distance = distance_approx(user_lat,dblat,user_log,dblog)
            if i>distance or i==0:
                i=distance
                closest_station = station

        if closest_station:
            serializer = StationSerializer(closest_station)
            data = serializer.data
            data['distance_km'] = round(i, 2)
            return Response(data)
        
        return Response({"error": "No stations found"}, status=404)





