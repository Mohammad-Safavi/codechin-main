from django.db import models
from django.contrib.auth.models import User
import datetime

class Keyword(models.Model):
	title = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title 

class Article(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	pic_link = models.CharField(max_length=400)
	slug = models.CharField(max_length=255)
	keywords = models.ManyToManyField(Keyword)
	body = models.TextField()
	status = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


