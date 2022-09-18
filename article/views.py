from django.shortcuts import render
from .serializers import *
from rest_framework import generics, viewsets
from .models import *
# Create your views here.

class ArticleViewSet(generics.ListAPIView,
	viewsets.GenericViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
