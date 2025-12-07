from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username
    
class Location(models.Model):
    latitude=models.DecimalField(max_digits=9,decimal_places=6)
    longitude=models.DecimalField(max_digits=9,decimal_places=6)
    state = models.CharField(max_length=20)
    local_government = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.address

class Security_Incident(models.Model):
    INCIDENT_TYPES = [
        ('ROBBERY', 'Robbery'),
        ('ACCIDENT', 'Accident'),
        ('RIOT', 'Riot'),
        ('KIDNAPPING', 'Kidnapping'),
        ('TERRORISM', 'Terrorism'),
        ('OTHER', 'Other'),
    ]
    incident_type=models.CharField(max_length=20,choices=INCIDENT_TYPES)
    description=models.TextField()
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    incident_date=models.DateField()
    reported_date=models.DateTimeField(auto_now_add=True)

class Security_Alert(models.Model):
    ALERT_LEVELS = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    description=models.TextField()
    alert_level=models.CharField(max_length=10,choices=ALERT_LEVELS)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    expires_at=models.DateTimeField()
class stations(models.Model):
    STATION_TYPES = [
        ('POLICE', 'Police Station'),
        ('MILITARY','Military'),
        ('HOSPITAL', 'Hospital'),
        ('FIRE', 'Fire Station'),
    ]
    STATUS=[
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Nonactive'),
    ]
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    type=models.CharField(max_length=10,choices=STATION_TYPES)
    status=models.CharField(max_length=10,choices=STATUS)
    contact=models.CharField(max_length=15, unique=True)

class High_Risk_Area(models.Model):
    RISK_LEVELS = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]
    INCIDENT_TYPES = [
        ('ROBBERY', 'Robbery'),
        ('ACCIDENT', 'Accident'),
        ('RIOT', 'Riot'),
        ('KIDNAPPING', 'Kidnapping'),
        ('TERRORISM', 'Terrorism'),
        ('OTHER', 'Other'),
    ]
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    risk_level=models.CharField(max_length=10,choices=RISK_LEVELS)
    risk_types=models.CharField(max_length=10,)
    updated_at=models.DateTimeField(auto_now=True)