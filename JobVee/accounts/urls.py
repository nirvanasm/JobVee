from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    #url(r'^account/login/$', login, {'template_name': 'accounts/login.html'} , name = 'login' ),
    url(r'^account/register/$', views.register, name = 'register'),
    url(r'^account/profile/$',views.view_profile, name = 'view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name = 'edit_profile'),

]