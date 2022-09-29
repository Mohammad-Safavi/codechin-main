from rest_framework import serializers
from .models import Article, Keyword
from core.serializers import UserSerializer
class KeywordSerializer(serializers.ModelSerializer):
	class Meta : 
		model = Keyword
		fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	keywords = KeywordSerializer(many=True)
	class Meta :
		model = Article
		fields = '__all__'