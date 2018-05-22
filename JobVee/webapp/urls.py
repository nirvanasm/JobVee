from django.conf.urls import url
from . import views

urlpatterns = [
    #Front Page
    url(r'^home', views.index, name='index'),

    #Account Page
    url(r'^account/login', views.login, name='login'),
    url(r'^account/forgot', views.forgotPass, name='forgotPass'),
    url(r'^account/userProfile', views.userProfile, name='userProfile'),
    url(r'^editProfile', views.editProfile, name='editProfile'),
    url(r'^account/register', views.register, name='register'),

    #Insert Data Apps
    url(r'^insertCompany', views.insertCompany, name='insertCompany'),
    url(r'^insertJob', views.insertJob, name='insertJob'),
    url(r'^insertProject', views.insertProject, name='insertProject'),
    url(r'^submitCompany', views.inputTest, name='inputTest'),
    url(r'^submitJob', views.inputJob, name='inputJob'),
    url(r'^submitProject', views.inputProject, name='inputProject'),
]