from django.contrib import admin
from django.urls import path, include
from core import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register('list', views.WorkSampleViewSet, basename='list')

urlpatterns = [
    path('', include(router.urls)),
]
