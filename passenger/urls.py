from . import views


urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    ]
