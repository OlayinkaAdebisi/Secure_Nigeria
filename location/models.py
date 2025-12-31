from django.db import models
from django.conf import settings

# Create your models here.
class Location(models.Model):
    STATE_CHOICES = (
    ('Abia', 'Abia'),
    ('Adamawa', 'Adamawa'),
    ('Akwa Ibom', 'Akwa Ibom'),
    ('Anambra', 'Anambra'),
    ('Bauchi', 'Bauchi'),
    ('Bayelsa', 'Bayelsa'),
    ('Benue', 'Benue'),
    ('Borno', 'Borno'),
    ('Cross River', 'Cross River'),
    ('Delta', 'Delta'),
    ('Ebonyi', 'Ebonyi'),
    ('Edo', 'Edo'),
    ('Ekiti', 'Ekiti'),
    ('Enugu', 'Enugu'),
    ('FCT', 'FCT'),
    ('Gombe', 'Gombe'),
    ('Imo', 'Imo'),
    ('Jigawa', 'Jigawa'),
    ('Kaduna', 'Kaduna'),
    ('Kano', 'Kano'),
    ('Katsina', 'Katsina'),
    ('Kebbi', 'Kebbi'),
    ('Kogi', 'Kogi'),
    ('Kwara', 'Kwara'),
    ('Lagos', 'Lagos'),
    ('Nasarawa', 'Nasarawa'),
    ('Niger', 'Niger'),
    ('Ogun', 'Ogun'),
    ('Ondo', 'Ondo'),
    ('Osun', 'Osun'),
    ('Oyo', 'Oyo'),
    ('Plateau', 'Plateau'),
    ('Rivers', 'Rivers'),
    ('Sokoto', 'Sokoto'),
    ('Taraba', 'Taraba'),
    ('Yobe', 'Yobe'),
    ('Zamfara', 'Zamfara'),
)

    REPORT_SOURCE_CHOICES = [
        ('EYEWITNESS', 'Eyewitness Report (I saw it)'),
        ('UNVERIFIED', 'Unverified Report (I heard about it)'),
        ('VERIFIED', 'Verified Security Report'), 
    ]
    INCIDENT_TYPES = [
        ('ROBBERY', 'Robbery'),
        ('ACCIDENT', 'Accident'),
        ('RIOT', 'Riot'),
        ('KIDNAPPING', 'Kidnapping'),
        ('TERRORISM', 'Terrorism'),
        ('OTHER', 'Other'),
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
    description = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    incident_types=models.CharField(max_length=10,choices=INCIDENT_TYPES, null=True, blank=True)
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
        ('INACTIVE', 'Inactive'),
    ]
    latitude = models.DecimalField(max_digits=9, decimal_places=6, db_column='latitude') 
    longitude = models.DecimalField(max_digits=9, decimal_places=6, db_column='longitude')
    state = models.CharField(max_length=50, null=True, blank=True,db_column='state')
    state_code = models.CharField(max_length=5, db_column='state_code', null=True, blank=True)
    lga = models.CharField(max_length=20, null=True, blank=True,db_column='lga')
    name=models.CharField(max_length=200, db_column='name')
    type=models.CharField(max_length=10,choices=STATION_TYPES, null=True, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, null=True, blank=True)
    contact=models.CharField(max_length=100, null=True, blank=True)
    timestamp=models.CharField(max_length=255,db_column='timestamp')
    address=models.TextField(null=True, blank=True, db_column='address')
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'stations'

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
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,limit_choices_to={'is_staff': True},)
    description=models.TextField(null=True, blank=True)
    risk_level=models.CharField(max_length=10,choices=RISK_LEVELS)
    risk_types=models.CharField(max_length=10,choices=INCIDENT_TYPES)
    updated_at=models.DateTimeField(auto_now=True)

class Feed(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=100, null=True, blank=True)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    risk_area = models.ForeignKey('High_Risk_Area', on_delete=models.CASCADE, null=True, blank=True)
    risk_level = models.CharField(max_length=100, null=True, blank=True)
    content=models.TextField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post=models.ForeignKey(Feed,on_delete=models.CASCADE,null=True, blank=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True, blank=True)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Verify(models.Model):
    post=models.ForeignKey(Feed,on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"