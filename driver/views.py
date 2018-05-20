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
