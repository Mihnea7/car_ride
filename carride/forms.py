from django import forms
from django.contrib.auth.models import User
from carride.models import UserProfile, Review, Vehicle

INTEGER_CHOICES= [tuple([x,x]) for x in range(0,10)]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class ReviewForm(forms.ModelForm):
	review = forms.CharField(max_length = 1024)
	rating = forms.DecimalField(decimal_places = 1, max_digits = 5)

	class Meta:
		model = Review
		fields = ('review', 'rating')

class rateForm(forms.ModelForm):
    widget=forms.Select(choices=INTEGER_CHOICES)
		
class VehicleForm(forms.ModelForm):
    make = forms.CharField(max_length=256, help_text="Car Make")
    model = forms.CharField(max_length = 256,
                            help_text='Please enter the car model')
    price = forms.DecimalField(decimal_places = 1, max_digits = 10, 
    	                       help_text='Please enter the price')
    year = forms.IntegerField(help_text='Please enter the Car year')
    new = forms.BooleanField(help_text='Is the Car New?', required=False)
    phoneNum = forms.CharField(help_text='Please Enter your Phone Number',
                               max_length = 13)
    additionalInfo = forms.CharField(help_text='please enter any additional information',
                                     max_length = 1024)
    
    
    class Meta:
        model = Vehicle
        fields = ('make', 'model', 'price', 'year', 'new', 'phoneNum',
                  'additionalInfo', 'picture')

