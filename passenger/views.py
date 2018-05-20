from django.shortcuts import render

# Create your views here.

def home(request):

    title = 'Passenger'
    return render(request, 'passenger/home.html', {'title':title})
