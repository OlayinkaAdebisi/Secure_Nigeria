from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    
    reported_by = serializers.ReadOnlyField(source='reported_by.username')
    class Meta:
        model = Location
        fields=['latitude','longitude','state','local_government','address','report_source','reported_by']