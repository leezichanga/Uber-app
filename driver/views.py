from django.shortcuts import render

# Create your views here.
def home(request, username):
    user = User.objects.get(username=username)
    driver_profile = DriverProfile.objects.get(user=user)
    carpool = CarPool.objects.filter(id=user.id)
    num_passengers = len(carpool)
    capacity = driver_profile.car_capacity
    print(carpool)
    print(num_passengers)
    if request.method == 'POST':
        carpool_form = CarPoolForm(request.POST)

        if carpool_form.is_valid() and num_passengers <= capacity:
            carpool_form.save()
            messages.success(request, ('You have a ride with this driver!'))
            return HttpResponseRedirect("/driver/%s"%user.username)
        else:
            messages.error(request, ('This car is full, try another driver.'))
    else:
        carpool_form = CarPoolForm()

    title = 'Driver'
    return render(request, 'driver/home.html', {'title':title, "user":user, "carpool":carpool, "form":carpool_form})

def profile(request, username):
    '''
    render driver information
    '''
    user = User.objects.get(username=username)
    profile = DriverProfile.objects.get(user=user)
    location = Location.objects.get(user=user)

    title = f"{user.username}"
    return render(request, 'driver/profile.html', {"user":user, "profile":profile, "location":location})

def update_profile(request, username):
    user = User.objects.get(username = username)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = DriverProfileForm(request.POST, instance=request.user.driverprofile, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return HttpResponseRedirect("/driver/profile/%s"%user.username)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = Udef update_profile(request, username):
    user = User.objects.get(username = username)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = DriverProfileForm(request.POST, instance=request.user.driverprofile, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return HttpResponseRedirect("/driver/profile/%s"%user.username)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance = request.user)
        profile_form = DriverProfileForm(instance = request.user.def update_profile(request, username):
    user = User.objects.get(username = username)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = DriverProfileForm(request.POST, instance=request.user.driverprofile, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return HttpResponseRedirect("/driver/profile/%s"%user.username)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance = request.user)
        profile_form = DriverProfileForm(instance = request.user.def update_profile(request, username):
    user = User.objects.get(username = username)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = DriverProfileForm(request.POST, instance=request.user.driverprofile, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return HttpResponseRedirect("/driver/profile/%s"%user.username)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance = request.user)
        profile_form = DriverProfileForm(instance = request.userdef update_profile(request, username):
    user = User.objects.get(username = username)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = DriverProfileForm(request.POST, instance=request.user.driverprofile, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return HttpResponseRedirect("/driver/profile/%s"%user.username)
        else:def update_profile(request, username):
    user = User.objects.get(username = username)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = DriverProfileForm(request.POST, instance=request.user.driverprofile, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return HttpResponseRedirect("/driver/profile/%s"%user.username)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance = request.user)
        profile_form = DriverProfileForm(instance = request.user.driverprofile)
    return render(request, 'driver/update_profile.html', {"user_form": user_form,"profile_form": profile_form})
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance = request.user)
        profile_form = DriverProfileForm(instance = request.user.driverprofile)
    return render(request, 'driver/update_profile.html', {"user_form": user_form,"profile_form": profile_form}).driverprofile)
    return render(request, 'driver/update_profile.html', {"user_form": user_form,"profile_form": profile_form})driverprofile)
    return render(request, 'driver/update_profile.html', {"user_form": user_form,"profile_form": profile_form})driverprofile)
    return render(request, 'driver/update_profile.html', {"user_form": user_form,"profile_form": profile_form})serForm(instance = request.user)
        profile_form = DriverProfileForm(instance = request.user.driverprofile)
    return render(request, 'driver/update_profile.html', {"user_form": user_form,"profile_form": profile_form})


def update_location(request, username):
    user = User.objects.get(username = username)

    if request.method == 'POST':
        location_form = LocationForm(request.POST, instance=request.user.driver_location)
        print(location_form)
        if location_form.is_valid():
            location_form.save()
            messages.success(request, ('You have updated your location.'))
            return HttpResponseRedirect("/driver/profile/%s"%user.username)
        else:
            messages.error(request, ('Please correct the error.'))
    else:
        location_form = LocationForm(instance=request.user.driver_location)

    title = 'Update Location'
    return render(request, 'driver/update_location.html', {"title":title, "form":location_form})

def find_passenger(request):
    passengers = PassengerProfile.objects.all()

    title = 'Find Passenger'
    return render(request, 'passenger/find_passenger.html', {"title":title, "passengers":passengers})

def driver_profile(request, passenger_id):
    user = User.objects.get(id=passenger_id)
    passenger_profile = PassengerProfile.objects.filter(user=user)

    title = 'Passenger Profile'
    return render(request, 'driver/passenger_profile.html', {"title":title, "profile":passenger_profile})
