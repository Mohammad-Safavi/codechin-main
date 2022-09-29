from django.shortcuts import render
from .serializers import *
from rest_framework import generics, viewsets
from .models import *
from app.helper.pagination import StandardResultsSetPagination

class ArticleViewSet(generics.ListAPIView, generics.RetrieveAPIView,
	viewsets.GenericViewSet):
	pagination_class = StandardResultsSetPagination
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
