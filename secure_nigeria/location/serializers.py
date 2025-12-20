from rest_framework import serializers
from .models import Location,Stations

class LocationSerializer(serializers.ModelSerializer):

    reported_by = serializers.ReadOnlyField(source='reported_by.username')
    class Meta:
        model = Location
        fields=['id','latitude','longitude','state','local_government','address','report_source','reported_by','description', 
            'created_at']

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stations
        fields=['id','name','address','lga','state','contact']