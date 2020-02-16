from django.db import models

# Create your models here.
class question(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField()

class repo(models.Model):
	repo