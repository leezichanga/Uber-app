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
        user_form = UserForm(instance = request.user)
        profile_form = DriverProfileForm(instance = request.user.driverprofile)
    return render(request, 'driver/update_profile.html', {"user_form": user_form,"profile_form": profile_form})
