from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Trial(models.Model):
	group = models.CharField(max_length = 2000)
	time = models.DateTimeField()
	subject = models.ForeignKey(User, related_name = "User")





