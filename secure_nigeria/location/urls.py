from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet,StationViewSet,RiskViewSet,FeedViewSet,CommentViewset,VerifyView,UnverifyView

router=DefaultRouter()
router.register(r'location',LocationViewSet)
router.register(r'station',StationViewSet)
router.register(r'risk',RiskViewSet)
router.register(r'feed',FeedViewSet)
router.register(r'comment',CommentViewset)

urlpatterns=[
    path('',include(router.urls)),
    path('feed/verify/<int:pk>/',VerifyView.as_view()),
    path('feed/unverify/<int:pk>/',UnverifyView.as_view()),
]