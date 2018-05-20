from django import forms
from django.contrib.auth.models import User
from driver.models import Reviews
from .models import PassengerProfile, Location, Reviews

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class PassengerProfileForm(forms.ModelForm):
    class Meta:
        model = PassengerProfile
        fields = ['profile_pic', 'gender', 'age']

class DriverReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('review',)

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['current', 'destination']
