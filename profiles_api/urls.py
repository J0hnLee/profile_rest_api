import imp
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('userProfile',views.UserProfileViewSet)

urlpatterns = [
    path('hello_view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
