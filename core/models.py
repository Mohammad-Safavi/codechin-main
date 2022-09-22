from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Picture(models.Model):

	title = models.CharField(max_length=255)
	link = models.TextField()

	def __str__(self):
		return self.title

class WorkSample(models.Model):

	title = models.CharField(max_length=255)
	description = models.TextField()
	picture = models.ManyToManyField(Picture)
	link = models.TextField()
	maintainers = models.ManyToManyField(User ,related_name = 'maintainers')
	designers = models.ManyToManyField(User ,related_name = 'designers')
	developers = models.ManyToManyField(User, related_name = 'developers')
	created_at = models.DateTimeField(auto_now_add=True)
	started_at = models.DateTimeField()
	ended_at = models.DateTimeField()

