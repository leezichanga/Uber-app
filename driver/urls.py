from django.conf import settings
from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^profile/$', views.profile, name='profile_view'),
    url(r'^profile/update/$', views.update_profile, name='update_profile_view'),
    url(r'^location/update/$', views.update_location, name='update_location_view'),
    url(r'^find_passenger/$', views.find_passenger, name='find_passenger'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
