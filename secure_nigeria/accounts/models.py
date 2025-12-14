from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    followers=models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
        )
    
    def __str__(self):
        return self.username

