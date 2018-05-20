from django.db import models

# Create your models here.
class PassengerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    profile_pic = models.ImageField(upload_to='profile/passenger/', default='/media/profile/passenger/user.svg', null=True)
    age = models.IntegerField(null=True)

    def getPic(self):
        if not self.profile_pic:
            return '/media/profile/driver/user.svg'

    # link to in-built user model
    @receiver(post_save,sender = User)
    def create_user_profile(sender,instance,created, **kwargs):
        if created:
            PassengerProfile.objects.create(user=instance)

    @receiver(post_save,sender = User)
    def save_user_profile(sender,instance,**kwargs):
        instance.passengerprofile.save()
    # end of link


class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='passenger_location')
    current = models.CharField(max_length=100, blank=True)
    destination = models.CharField(max_length=100, blank=True)

    # link to in-built user model
    @receiver(post_save,sender = User)
    def create_user_location(sender,instance,created, **kwargs):
        if created:
            Location.objects.create(user=instance)

    @receiver(post_save,sender = User)
    def save_user_location(sender,instance,**kwargs):
        instance.passenger_location.save()
    # end of link

class Reviews(models.Model):
    review = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='passenger_reviews')
