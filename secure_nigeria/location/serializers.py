from rest_framework import serializers
from .models import Location,Stations,High_Risk_Area,Feed,Comment

class LocationSerializer(serializers.ModelSerializer):

    reported_by = serializers.ReadOnlyField(source='reported_by.username')
    class Meta:
        model = Location
        fields=['id','latitude','longitude','state','local_government','address','reported_by','description', 
            'created_at','incident_types']

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stations
        fields=['id','name','address','lga','state','contact']

class RiskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model=High_Risk_Area
        fields=['id','location', 'user', 'description','risk_level','risk_types']

        read_only_fields = ['user', 'updated_at']

class FeedSerializer(serializers.ModelSerializer):
    author=serializers.ReadOnlyField(source='author.username')
    location_id=serializers.ReadOnlyField(source='location.id')
    class Meta:
        model=Feed
        fields=['id','author', 'title', 'content', 'location_id', 'risk_level','created_at']

        read_only_fields = ['author', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model=Comment
        fields=['id','user','post', 'content', 'created_at']

        read_only_fields = ['user', 'created_at']