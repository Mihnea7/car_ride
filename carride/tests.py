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

		car = Vehicle(make='Porsche', model='Macan',
					  numplate='BD51SMR', price=1000,
					  year=2019, new=False, phoneNum='07928962185',
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
					  year=2009, new=False, phoneNum='07928962185',
					  picture=ImageFile(open('media\\Ford_Fiesta_2009.jpg', 'rb')),
					  additionalInfo='blue colour', forSale=True)
		car.save()
		self.assertEqual(car.slug, 'ford-fiesta-hu51pek')

class SearchViewTests(TestCase):
	def test_search_no_such_make(self):
		'''
		If no such make exists in database, an appropriate message should be displayed
		'''
		response = self.client.get(reverse('search'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No cars exist with this make in our database.")
		self.assertQuerysetEqual(response.context['car_list'], [])

def add_car(make, model, numplate, price, year, new, username, phoneNum, info, picture, forSale):
	v = Vehicle.objects.get_or_create(model=model)[0]
	v.make=make
	v.numplate=numplate
	v.forSale= forSale
	v.price = price
	v.year = year
	v.new = new
	v.username = username
	v.phoneNum = phoneNum
	v.additionalInfo = info
	v.picture = picture
	v.save()
	return v

class BuyViewTests(TestCase):
	def test_buy_view_with_Vehicles(self):
		
		add_car(make='Porsche', model='Macan',
				numplate='BD51SMR', price=1000,
				year=2019, new=False, phoneNum='07928962185',
				picture=ImageFile(open('media\\Porsche-Macan-02.jpg', 'rb')),
				info='blue colour', forSale=True, username="Deni Nedjalkova")

		add_car(make='Tesla', model='S',
				numplate='BD51SMA', price=1000,
				year=2018, new=False, phoneNum='07928962185',
				picture=ImageFile(open('media\\tesla-s.jpg', 'rb')),
				info='blue colour', forSale=True, username="Deni Nedjalkova")

		add_car(make='Ford', model='Fiesta',
				numplate='BD51SMP', price=1000,
				year=2009, new=False, phoneNum='07928962185',
				picture=ImageFile(open('media\\Ford_Fiesta_2009.jpg', 'rb')),
				info='blue colour', forSale=True, username="Deni Nedjalkova")

		response = self.client.get(reverse('buy'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Macan")
		num_cars =len(response.context['buy_cars'])
		self.assertEqual(num_cars , 3)

