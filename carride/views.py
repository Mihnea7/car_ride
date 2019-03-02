from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from carride.models import Vehicle

# each view returns HttpResponse object - takes string
# as a parameter representing the content of the page 
# to be sent to the client

def show_car_details(request):
	context_dict = {}

	car = Vehicle.objects.order_by('-price')[0] # one dictionary

	context_dict['chosen_car'] = car

	response = render(request, 'carride/cardetails.html', context=context_dict)

	return response

def index(request):

	response = render(request, 'carride/base.html')

	return response