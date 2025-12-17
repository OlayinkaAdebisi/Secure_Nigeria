from django.db import models
from django.conf import settings

# Create your models here.
class Location(models.Model):
    STATE_CHOICES = [
        ('AB', 'Abia'), ('AD', 'Adamawa'), ('AK', 'Akwa Ibom'), ('AN', 'Anambra'),
        ('BA', 'Bauchi'), ('BY', 'Bayelsa'), ('BE', 'Benue'), ('BO', 'Borno'),
        ('CR', 'Cross River'), ('DE', 'Delta'), ('EB', 'Ebonyi'), ('ED', 'Edo'),
        ('EK', 'Ekiti'), ('EN', 'Enugu'), ('FC', 'FCT - Abuja'), ('GO', 'Gombe'),
        ('IM', 'Imo'), ('JI', 'Jigawa'), ('KD', 'Kaduna'), ('KN', 'Kano'),
        ('KT', 'Katsina'), ('KE', 'Kebbi'), ('KO', 'Kogi'), ('KW', 'Kwara'),
        ('LA', 'Lagos'), ('NA', 'Nasarawa'), ('NI', 'Niger'), ('OG', 'Ogun'),
        ('ON', 'Ondo'), ('OS', 'Osun'), ('OY', 'Oyo'), ('PL', 'Plateau'),
        ('RI', 'Rivers'), ('SO', 'Sokoto'), ('TA', 'Taraba'), ('YO', 'Yobe'),
        ('ZA', 'Zamfara'),
    ]

    REPORT_SOURCE_CHOICES = [
        ('EYEWITNESS', 'Eyewitness Report (I saw it)'),
        ('UNVERIFIED', 'Unverified Report (I heard about it)'),
        ('VERIFIED', 'Verified Security Report'), 
    ]

    latitude=models.DecimalField(max_digits=9,decimal_places=6)
    longitude=models.DecimalField(max_digits=9,decimal_places=6)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, null=True, blank=True)
    local_government = models.CharField(max_length=20)
    address = models.TextField()
    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    report_source = models.CharField(
        max_length=15, 
        choices=REPORT_SOURCE_CHOICES, 
        default='EYEWITNESS'
    )
    def __str__(self):
        return self.address
class Stations(models.Model):
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

    def __str__(self):
        return self.location