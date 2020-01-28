
from django.urls import path
from .views import login


app_name= "registration"
urlpatterns = [
     path('',login,name='login'),

      
]

