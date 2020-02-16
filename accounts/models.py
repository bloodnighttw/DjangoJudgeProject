from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your models here.
class models(models.Model):
	content = models.TextField(default = "bang")

	class Meta:
		db_table = "bang"

class form_with_email(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

			