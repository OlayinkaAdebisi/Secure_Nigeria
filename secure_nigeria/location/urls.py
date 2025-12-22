from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet,StationViewSet

router=DefaultRouter()
router.register(r'location',LocationViewSet)
router.register(r'station',StationViewSet)

urlpatterns=[
    path('',include(router.urls)),
]