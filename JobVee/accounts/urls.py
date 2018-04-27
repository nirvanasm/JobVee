from django.conf.urls import url
from accounts import views as view_account
from webapp import views as views_webapp
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views_webapp.index),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'} ),
    url(r'^register/$', view_account.register, name = 'register'),
    url(r'^profile/$',view_account.view_profile, name = 'view_profile'),
    url(r'^profile/edit/$', view_account.edit_profile, name = 'edit_profile'),
]