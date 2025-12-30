from django.urls import path,include
from .views import SignUpView,LoginView,ProfileView,FollowView,UnfollowView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'profile',ProfileView)

urlpatterns=[
    path('',include(router.urls)),
    path("signup/",SignUpView.as_view()),
    path("login/",LoginView.as_view()),
    path("follow/<int:pk>/",FollowView.as_view()),
    path("unfollow/<int:pk>/",UnfollowView.as_view()),
]