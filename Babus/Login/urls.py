
from django.urls import path
from .views import login


app_name= "Login"
urlpatterns = [
     path('',login,name='login'),

      
]

