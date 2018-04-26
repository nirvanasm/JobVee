from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'webapp/index.html')

def login(request):
    return render(request, 'webapp/account/login.html')

def forgotPass(request):
    return render(request, 'webapp/account/forgot.html')

def register(request):
    return render(request, 'webapp/account/register.html')

def searchJob(request):
    return render(request, 'webapp/searchJob.html')

def searchProject(request):
    return render(request, 'webapp/searchProject.html')

def editProfile(request):
    return render(request, 'webapp/account/editProfile.html')

def userProfile(request):
    return render(request, 'webapp/account/userProfile.html')

def userProfile(request):
    return render(request, 'webapp/account/userProfile.html')

def loginIndex(request):
    return render(request, 'webapp/login/loginIndex.html')

def loginSearchJob(request):
    return render(request, 'webapp/login/loginSearchJob.html')

def loginSearchProject(request):
    return render(request, 'webapp/login/loginSearchProject.html')

#This redirect function is for redirect to index.html
def redirectHome(request):
    return HttpResponseRedirect('webapp/index.html')

def redirectLoginHome(request):
    return HttpResponseRedirect('webapp/loginIndex.html')

# Geocode Google Maps API = AIzaSyBWixlVEt6g95dhEDj3ySSwEI_z_ciO9vM
# Distance Matrix Google API = AIzaSyCKUmrC5fneqMntGnGsEmZrzPIM33kRTIg