from django.conf import settings
from django.conf.urls import url
from . import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^passenger_profile/$', views.profile, name='profile'),
    url(r'^passenger_profile/update$', views.update_profile, name='update_profile'),
    url(r'^drivers/$', views.find_driver, name='find_driver'),
    url(r'^driver/profile/(\d+)$', views.driver_profile, name='driver_profile'),
    url(r'^driver/(\d+)/review/$', views.review_driver, name='review_driver'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
