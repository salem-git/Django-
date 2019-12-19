
from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
# Create your models here.

class Bus(models.Model):
     #inheritance
     
     name = models.CharField(max_length=50)
     description = models.TextField()
     
     def __str__(self):
          return self.name