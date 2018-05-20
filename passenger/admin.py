from django.contrib import admin
from .models import PassengerProfile, Location, Reviews

# Register your models here.
admin.site.register(PassengerProfile)
admin.site.register(Location)
admin.site.register(Reviews)
