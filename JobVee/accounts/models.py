from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import signals
# Create your models here.

class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete = models.CASCADE) #ada template database yg di import ke sini
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
    description = models.CharField(max_length = 100, default='')
    city = models.CharField(max_length = 50, default = '')
    email = models.EmailField(default='')
    website = models.URLField(default='')
    phone = models.CharField(max_length = 12, default = '')
    role = models.CharField(max_length = 10, default='employee')
    CV = models.FileField()
    project = models.FileField()
    objects = models.Manager() #kalo ga pake ini error pas create_profile
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
    instance.profile.save()

signals.post_save.connect(create_user_profile, sender=User)