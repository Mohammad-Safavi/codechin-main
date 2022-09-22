from django.shortcuts import render
from .serializers import *
from rest_framework import generics, viewsets
from .models import *
# Create your views here.

class WorkSampleViewSet(generics.ListAPIView,
	viewsets.GenericViewSet):
	queryset = WorkSample.objects.all()
	serializer_class = WorkSampleSerializer
