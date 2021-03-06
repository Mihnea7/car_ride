from django import forms
from django.contrib.auth.models import User
from carride.models import UserProfile, Review, Vehicle 

#INTEGER_CHOICES= [tuple([x,x]) for x in range(0,10)]

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

		
class VehicleForm(forms.ModelForm):
    make = forms.CharField(max_length=256, help_text="Car Make", required=True)
    model = forms.CharField(max_length = 256, help_text='Car model', required=True)
    numplate = forms.CharField(max_length = 10, help_text="Car Number Plate", required=True)
    price = forms.DecimalField(decimal_places = 1, max_digits = 10, 
    	                       help_text='Car Price (per day if for lease)', required=True)
    year = forms.IntegerField( help_text='Car year', required=True)
    new = forms.BooleanField(help_text='Is the Car New?', required=False)
    phoneNum = forms.CharField(help_text='Your Phone Number',
                               max_length = 13)
    picture = forms.ImageField(help_text='Add Picture of Car',required=True)
    username = forms.CharField(widget=forms.HiddenInput(),help_text='Enter Your Username',required=False)
    additionalInfo = forms.CharField(help_text='Additional information',
                                     max_length = 1024)
    forSale=forms.BooleanField(help_text='Tick if not for Lease', required=False)
    slug=forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Vehicle
        fields = ('make', 'model','numplate', 'price', 'year', 'new', 'phoneNum',
                  'username','additionalInfo', 'picture','forSale')


class CompareForm(forms.ModelForm):
    ID1= forms.IntegerField(help_text="ID of Car 1: ")
    ID2= forms.IntegerField(help_text="ID of Car 2: ")

    class Meta:
        model = Vehicle
        fields = ('ID',)

class SearchForm(forms.ModelForm):
    
    make = forms.CharField(max_length=256, help_text="Car Make", required=True)

    class Meta:
        model=Vehicle
        fields = ('make',)
