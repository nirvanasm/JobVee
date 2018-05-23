from django.conf.urls import url
from . import views
from accounts import views as views_account
from django.contrib.auth.views import login, logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    #Front Page
    url(r'^home', views.index, name='index'),

    #Account Page
    url(r'^logout', views.logout_user , name='logout'),
    url(r'^login', auth_views.login, {'template_name': 'webapp/account/login.html'}, name = 'login' ),
    url(r'^account/forgot', views.forgotPass, name='forgotPass'),
    url(r'^account/userProfile', views.userProfile, name='userProfile'),
    url(r'^account/editProfile', views_account.edit_profile, name='edit_profile'),
    url(r'^account/register', views_account.register, name='register'),

    #Insert Data Apps
    url(r'^insertCompany', views.insertCompany, name='insertCompany'),
    url(r'^insertJob', views.insertJob, name='insertJob'),
    url(r'^insertProject', views.insertProject, name='insertProject'),
    url(r'^submitCompany', views.inputTest, name='inputTest'),
    url(r'^submitJob', views.inputJob, name='inputJob'),
    url(r'^submitProject', views.inputProject, name='inputProject'),
]