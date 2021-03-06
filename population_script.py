import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					  'car_ride.settings')

import django
django.setup()
from carride.models import Vehicle
from django.core.files.images import ImageFile

def populate():

	car_info = [
	{"make":"Porsche",
     "model": "Macan S", "forSale": True, "numplate": "xxxx",
	 "price": 48750, "year": 2018, "new": True, "username": "Deni Nedjalkova", 
	 "phoneNum": "+447928962187", "additionalInfo": "blue colour",
	 "picture": ImageFile(open('media\\Porsche-Macan-02.jpg', 'rb')), },

	{"make":"Tesla",
     "model": "Model S", "forSale": False, "numplate": "xyyy",
	 "price": 73, "year": 2016, "new": True, "username": "Shourya Verma", 
	 "phoneNum": "+447928962185", "additionalInfo": "silver colour",
	 "picture": ImageFile(open('media\\tesla-s.jpg', 'rb')), },

    {"make":"Ford",
     "model": "Fiesta", "forSale": True, "numplate": "xxxz",
	 "price": 2300, "year": 2009, "new": False, "username": "Mihnea Maldaianu", 
	 "phoneNum": "+447928962333", "additionalInfo": "dark blue colour",
	 "picture": ImageFile(open('media\\Ford_Fiesta_2009.jpg', 'rb')), },

    {"make":"Volvo",
     "model": "740 Turbo", "forSale": True, "numplate": "xwxx",
	 "price": 10000, "year": 1985, "new": False, "username": "Alexander Cowan", 
	 "phoneNum": "+447333462187", "additionalInfo": "silver colour",
	 "picture": ImageFile(open('media\\volvo_740_1985_turbo.jpg', 'rb')), },
	]

	for c in car_info:
	 	add_car(c["make"], c["model"], c["numplate"], c["price"], c["year"], c["new"],
                                c["username"], c["phoneNum"], c["additionalInfo"], c["picture"], c["forSale"])

	for c in Vehicle.objects.all():
		print(c)

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

if __name__ == '__main__':
	print("Starting CarRide population script...")
populate()
