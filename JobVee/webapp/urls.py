from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home', views.index, name='index'),
    url(r'^account/login', views.login, name='login'),
    url(r'^account/forgot', views.forgotPass, name='forgotPass'),
    url(r'^account/userProfile', views.userProfile, name='userProfile'),
    url(r'^searchJob', views.searchJob, name='searchJob'),
    url(r'^searchProject', views.searchProject, name='searchProject'),
    url(r'^editProfile', views.editProfile, name='editProfile'),
    url(r'^account/register', views.register, name='register'),
    url(r'^loginSearchJob', views.loginSearchJob, name='loginSearchJob'),
    url(r'^loginSearchProject', views.loginSearchProject, name='loginSearchProject'),
    url(r'^loginHome', views.loginIndex, name='loginHome'),
]