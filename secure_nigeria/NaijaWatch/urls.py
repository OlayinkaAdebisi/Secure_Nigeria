from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView, # This is the Login View
    TokenRefreshView,
)

urlpatterns=[
    path('api/register/',RegisterView.as_view(),name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]