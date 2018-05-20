from . import views


urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^passenger_profile/(?P<username>[-_\w.]+)$', views.profile, name='profile'),
    ]
