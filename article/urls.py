from django.contrib import admin
from django.urls import path, include
from article import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register('list', views.ArticleViewSet, basename='list')

urlpatterns = [
    path('', include(router.urls)),
]
