from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .models import PassengerProfile, Location, Reviews
from driver.models import DriverProfile

# Create your views here.

def home(request):

    title = 'Passenger'
    return render(request, 'passenger/home.html', {'title':title})

def profile(request, username):
    '''
    render passenger information
    '''
    user = User.objects.get(username=username)
    profile = PassengerProfile.objects.get(user=user)
    location = Location.objects.get(user=user)

    title = f"{user.username}"
    return render(request, 'passenger/profile.html', {"user":user, "profile":profile, "location":location})

def update_profile(request, username):
    user = User.objects.get(username = username)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = PassengerProfileForm(request.POST, instance=request.user.passengerprofile, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return HttpResponseRedirect("/passenger/passenger_profile/%s"%user.username)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance = request.user)
        profile_form = PassengerProfileForm(instance = request.user.passengerprofile)

    title = 'Update Profile'
    return render(request, 'passenger/update_profile.html', {"title":title, "user_form": user_form, "profile_form": profile_form})

def find_driver(request):
    drivers = DriverProfile.objects.all()

    title = 'Find Driver'
    return render(request, 'passenger/find_driver.html', {"title":title, "drivers":drivers})

def driver_profile(request, driver_id):
    user = User.objects.get(id=driver_id)
    driver_profile = DriverProfile.objects.filter(user=user)

    title = 'Driver Profile'
    return render(request, 'passenger/driver_profile.html', {"title":title, "profile":driver_profile})

def review_driver(request):
    user = User.objects.get(id=driver_id)
    driver_profile = DriverProfile.objects.filter(user=user)
    pass
