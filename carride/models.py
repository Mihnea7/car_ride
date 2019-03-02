from django.db import models

# Create your models here.

class Vehicle(models.Model):
	model = models.CharField(max_length = 256, unique=True)
	price = models.DecimalField(decimal_places = 1, max_digits = 10, max_length = 10, null=True)
	year = models.IntegerField(null=True)
	new = models.BooleanField(default=True)
	username = models.CharField(max_length = 20, blank=True)
	phoneNum = models.CharField(max_length = 13, blank=True)
	additionalInfo = models.CharField(max_length = 1024)

	def __str__(self):
	# generate string representation of the class
		return self.model
