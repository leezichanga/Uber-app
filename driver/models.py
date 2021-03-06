from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class DriverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'profile/driver/', default='/media/profile/driver/user.svg', null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    car_capacity = models.IntegerField(null=True)
    plates = models.CharField(max_length=30, null=True)
    car_color = models.CharField(max_length=30, null=True)

    def getPic(self):
        if not self.profile_pic:
            return '/media/profile/driver/user.svg'

    # link to in-built user model
    @receiver(post_save,sender = User)
    def create_user_profile(sender,instance,created, **kwargs):
        if created:
            DriverProfile.objects.create(user=instance)

    @receiver(post_save,sender = User)
    def save_user_profile(sender,instance,**kwargs):
        instance.driverprofile.save()
    # end of link


class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver_location')
    current = models.CharField(max_length=100, blank=True)
    destination = models.CharField(max_length=100, blank=True)

    # link to in-built user model
    @receiver(post_save,sender = User)
    def create_user_location(sender,instance,created, **kwargs):
        if created:
            Location.objects.create(user=instance)

    @receiver(post_save,sender = User)
    def save_user_location(sender,instance,**kwargs):
        instance.driver_location.save()
    # end of link

class CarPool(models.Model):
    name = models.CharField(max_length=50, blank=True)
    destination = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Reviews(models.Model):
    review = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver_reviews')
