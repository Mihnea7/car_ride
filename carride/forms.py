from django import forms
from django.contrib.auth.models import User
from carride.models import UserProfile, Review

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
	review = forms.CharField(max_length = 1024, help_text="Please enter your review")
	rating = forms.DecimalField(decimal_places = 1, max_digits = 5)

	class Meta:
		model = Review
		fields = ('review', 'rating')