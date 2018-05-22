import googlemaps
from django.db import models
from django.conf import settings

# Create your models here.
class MsCompany(models.Model):
    name = models.CharField(max_length = 30, default='')
    address = models.CharField(max_length = 100, default='')
    lat = models.FloatField()
    lng = models.FloatField()
    objects = models.Manager()

    def __str__(self):
        return self.name

    def insertData(compName, compAddress):
        gmaps = googlemaps.Client(key='AIzaSyBWixlVEt6g95dhEDj3ySSwEI_z_ciO9vM')
        geocode_result = gmaps.geocode(compAddress)
        compLat = geocode_result[0]["geometry"]["location"]["lat"]
        compLng = geocode_result[0]["geometry"]["location"]["lng"]
        temp = MsCompany(name = compName, address = compAddress, lat = compLat, lng = compLng)
        temp.save()


class Applicant(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE, unique = True)

    def __str__(self):
        return self.user_id

class Job(models.Model):
    company_id = models.ForeignKey(MsCompany, on_delete = models.CASCADE)
    description = models.CharField(max_length = 1000, default = 'No Description')
    role = models.CharField(max_length = 20, default = '')
    salary = models.IntegerField()

    def __str__(self):
        return self.company_id.name, self.role

    def insertData(inpName, jobRole, jobSalary, jobDescription):
        compId = MsCompany.objects.get(name = inpName)
        temp = Job(company_id = compId, role = jobRole, salary = jobSalary, description = jobDescription)
        temp.save()


class ApplyJob(models.Model):
    applicant_id = models.ForeignKey(Applicant, on_delete = models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete = models.CASCADE)

class Project(models.Model):
    title = models.CharField(max_length = 20, default = '')
    deadline = models.DateField()
    wage = models.IntegerField()
    description = models.CharField(max_length = 1000, default = '')

    def insertData(projectTitle, projectDeadline, projectWage, projectDescription):
        temp = Project(wage = projectWage, deadline = projectDeadline, description = projectDescription, title = projectTitle)
        temp.save()

