from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class VisiProg(models.Model):
	group = models.CharField(max_length = 200)
	subject = models.ForeignKey(User, related_name = "User")

