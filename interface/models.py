from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validateGroup(value):
	try:
		a = [int(s) for s in value.lsplit().split(" ")]
		print a
		if len(a) != 9:
			raise ValidationError("Wrong number of entries in group")
	except ValidationError, err:
		raise err

# Create your models here.
class Trial(models.Model):
	group = models.CharField(max_length = 2000, validators = [validateGroup])
	time = models.DateTimeField()
	subject = models.ForeignKey(User, related_name = "User")





