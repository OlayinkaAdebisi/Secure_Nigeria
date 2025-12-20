from django.contrib import admin
from .models import Location,Stations
# Register your models here.

admin.site.register(Stations)
admin.site.register(Location)