
from django.urls import path
from .views import  logged


app_name= "CustomerHome"
urlpatterns = [
     path('',logged,name='CustomerHome'),
      
]

