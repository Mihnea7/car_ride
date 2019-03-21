
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(models.Model):
# This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
# The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True) 

    def __str__(self):
        return self.user.username

class Vehicle(models.Model):
	slug = models.SlugField()
	model = models.CharField(max_length = 256)
	ID = models.AutoField(primary_key= True)
	make = models.CharField(max_length = 256)
	price = models.DecimalField(validators=[MinValueValidator(0)], decimal_places = 1, max_digits = 10, null=True)
	year = models.IntegerField(validators=[MinValueValidator(1900),MaxValueValidator(2019)], null=True)
	new = models.BooleanField(default=True)
	username = models.CharField(max_length = 20, blank=True)
	phoneNum = models.CharField(max_length = 13, blank=True)
	additionalInfo = models.CharField(max_length = 1024)
	picture = models.ImageField(upload_to='car', blank=True, null=True)
	forSale= models.BooleanField(default=True)
	rating = models.DecimalField(decimal_places = 1, max_digits = 10,null=True)
	numplate = models.CharField(max_length = 10, null=True, unique=True)

	def save(self, *args, **kwargs):
            to_slugify = "%s-%s-%s" % (self.make, self.model, self.numplate)
            self.slug = slugify(to_slugify)
            super(Vehicle, self).save(*args, **kwargs)
		
	def __str__(self):
	# generate string representation of the class
		return self.model

class Review(models.Model):
	post = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	review = models.CharField(max_length = 1024)
	rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)], null=True)
	created_date = models.DateTimeField(default=timezone.now)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.review
