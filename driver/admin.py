from django.contrib import admin
from .models import DriverProfile, CarPool, Location, Reviews

# Register your models here.

admin.site.register(DriverProfile)
admin.site.register(CarPool)
admin.site.register(Location)
admin.site.register(Reviews)
