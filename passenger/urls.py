from django.conf import settings
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^passenger_profile/(?P<username>[-_\w.]+)$', views.profile, name='profile'),
    url(r'^passenger_profile/(?P<username>[-_\w.]+)/update/$', views.update_profile, name='update_profile'),
    url(r'^drivers/$', views.find_driver, name='find_driver'),
    url(r'^driver/profile/(\d+)$', views.driver_profile, name='driver_profile'),
    url(r'^driver/(\d+)/review/$', views.review_driver, name='review_driver'),
    ]
