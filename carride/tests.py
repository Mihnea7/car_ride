from django.test import TestCase
from carride.models import Vehicle
from django.core.files.images import ImageFile
from django.core.urlresolvers import reverse
import random

class VehicleMethodTests(TestCase):
	def test_ensure_price_is_positive(self):
	
		'''
		ensure_price_is_positive should result True for Vehicles 
		where price is zero or positive
		'''

		car = Vehicle(make='Volkswagen', model='Golf',
					  numplate='BD51SMR', price=1000,
					  year=2020, new=False, phoneNum='07928962185',
					  picture=ImageFile(open('media\\Porsche-Macan-02.jpg', 'rb')),
					  additionalInfo='blue colour', forSale=True)
		car.save()

		# all_cars = Vehicle.objects.all()
		# print (all_cars)
		# rand_i = random.randint(0, len(all_cars)-1)
		self.assertEqual((car.price >= 0), True)

	def test_slug_line_creation(self):
		
		'''
		slug_line_creation checks to make sure that when we add a Vehicle
		an appropriate slug line is created
		'''
		car = Vehicle(make='Ford', model='Fiesta',
					  numplate='HU51PEK', price=1000,
					  year=2020, new=False, phoneNum='07928962185',
					  picture=ImageFile(open('media\\Porsche-Macan-02.jpg', 'rb')),
					  additionalInfo='blue colour', forSale=True)
		car.save()
		self.assertEqual(car.slug, 'volkswagen-golf-HU51PEK')

class ShowCarDetailsViewTests(TestCase):
	#p214 of Django tutorial
