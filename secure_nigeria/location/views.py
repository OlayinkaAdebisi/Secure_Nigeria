from django.shortcuts import render
from .models import Location,Stations
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .serializers import LocationSerializer,StationSerializer
import math
# Create your views here.

def distance_approx(lat1,lon1,lat2,lon2):
# i used the  Haversine formula to approximate distance between two coordinates(lattitude n longitude)
    R = float(6371.00) #radius of earth (km)
# to radian
    la1=(float(lat1)*math.pi)/180
    la2=(float(lat2)*math.pi)/180
    lo1=(float(lon1)*math.pi)/180
    lo2=(float(lon2)*math.pi)/180
# difference between point 1 and 2
    lat=float(la2-la1)
    lon=float(lo2-lo1)
# a = sin²(Δφ/2) + cos(φ₁) * cos(φ₂) * sin²(Δλ/2)
    a = (math.sin(lat/2) ** 2) + math.cos(la1) * (math.cos(la2) * math.sin(lon/2)**2)
#c = 2 * atan2(√a, √(1-a)) or c = 2 * asin(√a)
    c = 2 * math.atan2((math.sqrt(a)), (math.sqrt(1-a)))

    d = float(R * c)
    return d


class LocationViewSet(viewsets.ModelViewSet):
    queryset=Location.objects.all()
    serializer_class=LocationSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)

    def create(self, request, *args, **kwargs):

        response = super().create(request, *args, **kwargs)
        user_lat = response.data.get('latitude') 
        user_log = response.data.get('longitude')

        try:
            lat=float(user_lat)
            log=float(user_log)
        except(ValueError, TypeError):
            return response
        i=float('inf')
        closest_station = None
        for station in Stations.objects.all():
            if station.latitude == None or  station.longitude==None:
                        continue

            try:
                dblat=float(station.latitude)
                dblog=float(station.longitude)
                distance = distance_approx(lat, log, dblat, dblog)
                
                if i>distance or i==0:
                    i=distance
                    closest_station = station

            except ValueError:
                pass

        if closest_station:
            serializer = StationSerializer(closest_station)
            data = serializer.data
            data['distance_km'] = round(i, 2)
            response.data['nearest_station'] = data
        
        return response

class StationViewSet(viewsets.ModelViewSet):
    queryset=Stations.objects.all()
    serializer_class=StationSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]



