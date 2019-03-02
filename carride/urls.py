from django.conf.urls import url
from carride import views

urlpatterns = [
	# allows to call the function url and point to the index view
	# for the mapping in urlpatterns
	url(r'^cardetails/', views.show_car_details, name='cardetails'),
]