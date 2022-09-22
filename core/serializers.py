from rest_framework import serializers
from .models import WorkSample, Picture
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	
	class Meta :
		model = User
		fields = '__all__'

class PictureSerializer(serializers.ModelSerializer):
	
	class Meta :
		model = Picture
		fields = '__all__'

class WorkSampleSerializer(serializers.ModelSerializer):
	picture = PictureSerializer(many=True)
	maintainers = UserSerializer(many=True)
	designers = UserSerializer(many=True)
	developers = UserSerializer(many=True)
	
	class Meta :
		model = WorkSample
		fields = '__all__'