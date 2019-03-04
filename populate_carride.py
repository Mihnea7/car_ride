import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					  'car_ride.settings')

import django
django.setup()
from carride.models import Vehicle

def populate():

	car_info = [
	{"model": "Porsche The new Macan S", 
	 "price": 48750, "year": 2018, "new": True, "username": "", 
	 "phoneNum": "+447928962187", "additionalInfo": "blue colour"},
	{"model": "Tesla Model S",
	 "price": 73500, "year": 2016, "new": True, "username": "", 
	 "phoneNum": "+447928962185", "additionalInfo": "silver colour"}
	]

	for c in car_info:
	 	add_car(c["model"], c["price"], c["year"], c["new"],
	 			c["username"], c["phoneNum"], c["additionalInfo"])

	for c in Vehicle.objects.all():
		print(c)

def add_car(model, price, year, new, username, phoneNum, info):
	v = Vehicle.objects.get_or_create(model=model)[0]
	v.price = price
	v.year = year
	v.new = new
	v.username = username
	v.phoneNum = phoneNum
	v.additionalInfo = info
	v.save()
	return v

if __name__ == '__main__':
	print("Starting CarRide population script...")
	populate()
