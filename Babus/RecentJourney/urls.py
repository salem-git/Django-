
from django.urls import path
from .views import  recentJourney


app_name= "RecentJourney"
urlpatterns = [
     path('',recentJourney,name='RecentJourney'),
      
]

