from django.urls import path,include
from .views import NotificationViewSet
from rest_framework.routers import DefaultRouter

urlpatterns=[
    path('notification/',NotificationViewSet.as_view())
    ]