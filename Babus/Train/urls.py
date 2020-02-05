
from django.urls import path
from .views import train  


app_name= "Train"
urlpatterns = [
     path('',train,name='train'),
      
]

