from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from searchApps.models import MsCompany, Job

startTemplate = 'webapp/header.html'
loginTemplate = 'webapp/loginHeader.html'

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'webapp/index.html', {'base_template': loginTemplate})    
    return render(request, 'webapp/index.html', {'base_template': startTemplate})

#View dealing with account login and registration
def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('../home')
    return render(request, 'webapp/account/login.html')

def forgotPass(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('../home')
    return render(request, 'webapp/account/forgot.html')

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('../home')
    return render(request, 'webapp/account/register.html')

#View dealing with user profile
def editProfile(request):
    if request.user.is_authenticated:
        return render(request, 'webapp/account/editProfile.html')
    return HttpResponseRedirect('../home')

def userProfile(request):
    if request.user.is_authenticated:
        return render(request, 'webapp/account/userProfile.html')
    return HttpResponseRedirect('../home')

#View that deal with database insert
def inputTest(request):
    companyName = request.POST.get("companyName")
    companyAddress = request.POST.get("companyAddress")
    MsCompany.insertData(companyName, companyAddress)
    return render(request, 'webapp/insertCompany.html', {'info': "Success Add "+companyName,})

def inputJob(request):
    companyName = request.POST.get("companyName")
    jobRole = request.POST.get("jobRole")
    jobSalary = request.POST.get("jobSalary")
    Job.insertData(companyName, jobRole, jobSalary)
    return render(request, 'webapp/insertJob.html', {'info': "Success Add",})
    
def insertCompany(request):
    return render(request, 'webapp/insertCompany.html')

def insertJob(request):
    return render(request, 'webapp/insertJob.html')

#This redirect function is for redirect to index.html
def redirectHome(request):
    return HttpResponseRedirect('index')

# Geocode Google Maps API = AIzaSyBWixlVEt6g95dhEDj3ySSwEI_z_ciO9vM
# Distance Matrix Google API = AIzaSyCKUmrC5fneqMntGnGsEmZrzPIM33kRTIg