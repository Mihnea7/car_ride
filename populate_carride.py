import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					  'car_ride.settings')

import django
django.setup()
from carride.models import Vehicle
from django.core.files.images import ImageFile

def populate():

	car_info = [
	{"model": "Porsche The new Macan S", 
	 "price": 48750, "year": 2018, "new": True, "username": "", 
	 "phoneNum": "+447928962187", "additionalInfo": "blue colour",
	 "picture": ImageFile(open('media\\Porsche-Macan-02.jpg', 'rb')), },
	{"model": "Tesla Model S",
	 "price": 73500, "year": 2016, "new": True, "username": "", 
	 "phoneNum": "+447928962185", "additionalInfo": "silver colour",
	 "picture": ImageFile(open('media\\tesla-s.jpg', 'rb')), },
	]

	for c in car_info:
	 	add_car(c["model"], c["price"], c["year"], c["new"],
	 			c["username"], c["phoneNum"], c["additionalInfo"], c["picture"])

	for c in Vehicle.objects.all():
		print(c)

def add_car(model, price, year, new, username, phoneNum, info, picture):
	v = Vehicle.objects.get_or_create(model=model)[0]
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