from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<username>[-_\w.]+)$', views.home, name='home'),
    url(r'^profile/(?P<username>[-_\w.]+)$', views.profile, name='profile_view'),
    url(r'^profile/(?P<username>[-_\w.]+)/update/$', views.update_profile, name='update_profile_view'),
    url(r'^location/(?P<username>[-_\w.]+)/update/$', views.update_location, name='update_location_view'),
    url(r'^find_passenger/$', views.find_passenger, name='find_passenger'),
    ]
