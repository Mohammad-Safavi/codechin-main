from django.shortcuts import render
from .serializers import *
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .models import *
from app.helper.pagination import StandardResultsSetPagination
# Create your views here.

class WorkSampleViewSet(generics.ListAPIView, generics.RetrieveAPIView,
	viewsets.GenericViewSet):
	pagination_class = StandardResultsSetPagination
	queryset = WorkSample.objects.all()
	serializer_class = WorkSampleSerializer

class RegisterGetCode(APIView):

	def post(self, request):
		# serializer = RegisterCodeSerializer(data=request.data)
	 #    serializer.is_valid(raise_exception=True)
	 #    phone = serializer.validated_data["phone"]
	 #    print(phone)
	 pass
