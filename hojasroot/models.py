from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    community = models.ForeignKey('Community', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)





class Community(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    




class Workplace(models.Model):

    pass




class Needs(models.Model):

    pass



class Projects(models.Model):
   
    pass 
