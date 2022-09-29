from django.contrib import admin
from django.urls import path, include
from core import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register('work-sample', views.WorkSampleViewSet, basename='list-worksample')

urlpatterns = [
    path('', include(router.urls)),
    path('register/get-code/' , views.RegisterGetCode.as_view(), name='code-number'),
    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
    
