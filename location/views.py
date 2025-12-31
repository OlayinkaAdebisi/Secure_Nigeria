from django.shortcuts import render
from .models import Location,Stations,High_Risk_Area,Feed,Comment,Verify
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions,generics,status
from .serializers import LocationSerializer,StationSerializer,RiskSerializer,FeedSerializer,CommentSerializer
import math
from alert.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
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
            data = dict(serializer.data)
            data['distance_km'] = round(i, 2)
            response.data['nearest_station'] = data
        else:
            print("No nearby station found.")
        return response

class StationViewSet(viewsets.ModelViewSet):
    queryset=Stations.objects.all()
    serializer_class=StationSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

class RiskViewSet(viewsets.ModelViewSet):
    queryset=High_Risk_Area.objects.all()
    serializer_class=RiskSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # get the descriptions from location

        risk_level = None
        risk_type = None
        for location in Location.objects.all():

            if location.incident_types == "TERRORISM":
                risk_level = 'HIGH'
                risk_type = 'TERRORISM'
            elif location.incident_types == "KIDNAPPING":
                risk_level = 'HIGH'
                risk_type = 'KIDNAPPING'
            elif location.incident_types == "ROBBERY":
                risk_level = 'MEDIUM'
                risk_type = 'ROBBERY'
            elif location.incident_types == "ACCIDENT":
                risk_level = 'MEDIUM'
                risk_type = 'ACCIDENT'
            elif location.incident_types == "RIOT":
                risk_level = 'LOW'
                risk_type = 'RIOT'
            else:
                risk_level = 'MEDIUM'
                risk_type = 'OTHER'

            High_Risk_Area.objects.update_or_create(
                location_id=location.id,
                defaults={
                    'user': request.user,
                    'description': location.description,
                    'risk_level': risk_level,
                    'risk_types': risk_type,
                }
            )

        return response
            
class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all().order_by('-created_at')
    serializer_class=FeedSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        feed=serializer.save(author=self.request.user)
        user= self.request.user
        Notification.objects.create(
                recipient=feed.author,
                actor=user,
                verb=f"{user.username} made a new post",
                content_type=ContentType.objects.get_for_model(Feed),
                object_id=feed.id
            )
    def list(self, request, *args, **kwargs):

        for risk in High_Risk_Area.objects.all():
            Feed.objects.update_or_create(
                risk_area=risk,
                defaults={
                'author': getattr(risk.location, 'reported_by', request.user),
                'title':risk.description,
                'location': risk.location,
                'created_at':risk.location.created_at,
                'risk_level': risk.risk_level,
                'content': (
                            f"{risk.description} at {risk.location.address}, "
                            f"{risk.location.local_government}, {risk.location.state}. "
                            f"Lat: {risk.location.longitude}, Long: {risk.location.latitude}. "
                            f"{risk.location.detail or ''}"
                        )
                }
            )

        return super().list(request, *args, **kwargs)

class CommentViewset(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        comment=serializer.save(user=self.request.user)
        feed=comment.post
        user= self.request.user
        Notification.objects.create(
                recipient=feed.author,
                actor=user,
                verb='Commented on your post',
                content_type=ContentType.objects.get_for_model(Feed),
                object_id=feed.id
            )

class VerifyView(generics.GenericAPIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request, pk):
        feed=generics.get_object_or_404(Feed,pk=pk)
        user=request.user
        verify,created=Verify.objects.get_or_create(user=user,post=feed)
        if created==False:
            return Response(
                {"message": "You already verified this post!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        Notification.objects.create(
                recipient=feed.author,
                actor=user,
                verb='verified your post',
                content_type=ContentType.objects.get_for_model(Feed),
                object_id=feed.id
            )

        return Response(
            {"message": "You verified this post!"},
            status=status.HTTP_201_CREATED
        )
class UnverifyView(generics.GenericAPIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request, pk):
        feed=generics.get_object_or_404(Feed,pk=pk)
        user=request.user
        try:
            verify=Verify.objects.get(user=user,post=feed)
            verify.delete()

            return Response(
                {"message":"You Unverified this post"},
                status=status.HTTP_200_OK
            )
        except Verify.DoesNotExist:
            return Response(
                {"message":"You haven't Verified this post"},
                status=status.HTTP_404_NOT_FOUND
            )