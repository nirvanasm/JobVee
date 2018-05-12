import googlemaps
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q, F
from .models import Job
from .sortingCmp import sortByDist


# Create your views here.

startTemplate = 'webapp/header.html'
loginTemplate = 'webapp/loginHeader.html'

#View dealing with main apps
def searchJobLoc(request):
    counter = Job.objects.count()
    if request.method == "GET":
        strKeyWord = request.GET.get('keyword')
        if strKeyWord in [None,'']:
            job = Job.objects.all()
            pass    
        else:
            gmaps = googlemaps.Client(key='AIzaSyBWixlVEt6g95dhEDj3ySSwEI_z_ciO9vM')
            geocode_result = gmaps.geocode(strKeyWord)
            centerLat = geocode_result[0]["geometry"]["location"]["lat"]
            centerLng = geocode_result[0]["geometry"]["location"]["lng"]
            job = Job.objects.all().annotate(dist = 
                            ((F('company_id__lat') - centerLat)**2) +
                            ((F('company_id__lng') - centerLng)**2)).order_by('dist')
    else:
        job = Job.objects.all()
        
    if request.user.is_authenticated:
        return render(request, 'webapp/searchJobLoc.html', {'jobList' : job, 'info': counter, 'base_template': loginTemplate,})
    return render(request, 'webapp/searchJobLoc.html', {'jobList' : job, 'info': counter, 'base_template': startTemplate,})

def searchJobKey(request):
    if request.method == "GET":
        strKeyWord = request.GET.get('keyword')
        if strKeyWord in [None,'']:
            job = Job.objects.all()
            counter = Job.objects.count()    
        else:
            job = Job.objects.filter(Q(role__contains = strKeyWord) | Q(company_id__name__contains = strKeyWord) | Q(company_id__address__contains = strKeyWord))
            counter = Job.objects.filter(Q(role__contains = strKeyWord) | Q(company_id__name__contains = strKeyWord) | Q(company_id__address__contains = strKeyWord)).count()
    else:
        job = Job.objects.all()
        counter = Job.objects.count()
    
    if request.user.is_authenticated:
        return render(request, 'webapp/searchJobKey.html', {'jobList' : job, 'info': counter, 'base_template': loginTemplate,})
    return render(request, 'webapp/searchJobKey.html', {'jobList' : job, 'info': counter, 'base_template': startTemplate,})

def searchProject(request):
    if request.user.is_authenticated:
        return render(request, 'webapp/searchProject.html', {'base_template': loginTemplate,})
    return render(request, 'webapp/searchProject.html', {'base_template': startTemplate,})
