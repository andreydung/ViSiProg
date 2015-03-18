from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Trial(models.Model):
	group = models.CharField(max_length = 4000)
	time = models.DateTimeField()
	subject = models.ForeignKey(User)

# Create your models here.
class TrialLLNL2(models.Model):
	group = models.CharField(max_length = 100000)
	time = models.DateTimeField()
	subject = models.ForeignKey(User)

# Create your models here.
class TrialLLNL3(models.Model):
	group = models.CharField(max_length = 100000)
	time = models.DateTimeField()
	subject = models.ForeignKey(User)

# Create your models here.
class TrialCOLOR(models.Model):
	group = models.CharField(max_length = 100000)
	time = models.DateTimeField()
	subject = models.ForeignKey(User)

# Create your models here.
class TrialBuilding(models.Model):
	group = models.CharField(max_length = 100000)
	time = models.DateTimeField()
	subject = models.ForeignKey(User)


