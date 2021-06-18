from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.

class User(AbstractUser):
    pass



class Lead(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey('Agent',on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name

class LeadProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)

class Agent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username


def set_profile(sender,instance,created,**kwargs):
    #print(instance.last_name)
    if created:
        LeadProfile.objects.create(first_name=instance.first_name,last_name=instance.last_name,age=instance.age)


post_save.connect(set_profile,sender=Lead)
