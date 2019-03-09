from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone

class UserProfile(models.Model):
# This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    
# The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username

class Vehicle(models.Model):
	model = models.CharField(max_length = 256, unique=True)
	make = models.CharField(max_length = 256, null=True)
	price = models.DecimalField(decimal_places = 1, max_digits = 10, null=True)
	year = models.IntegerField(null=True)
	new = models.BooleanField(default=True)
	username = models.CharField(max_length = 20, blank=True)
	phoneNum = models.CharField(max_length = 13, blank=True)
	additionalInfo = models.CharField(max_length = 1024)
	picture = models.ImageField(upload_to='car')
	slug = models.SlugField(unique=True, blank=True, null=True)
	forSale= models.BooleanField(default=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.model)
		super(Vehicle, self).save(*args, **kwargs)

	def __str__(self):
	# generate string representation of the class
		return self.model

class Review(models.Model):
	#post = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	review = models.CharField(max_length = 1024)
	rating = models.DecimalField(decimal_places = 1, max_digits = 5, null=True)
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.review
