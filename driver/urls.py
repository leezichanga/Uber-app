from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<username>[-_\w.]+)$', views.home, name='home'),
    url(r'^profile/(?P<username>[-_\w.]+)$', views.profile, name='profile_view'),
    ]
