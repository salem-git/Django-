from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Journey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    destination = models.CharField(max_length=50)
    departure = models.CharField(max_length=50)
    number_of_ticket = models.IntegerField(null=True)
    seat_number = models.IntegerField(null=True)
    date = models.DateField()
     
    def __str__(self):
          return self.destination