
from django.urls import path
from .views import signup  


app_name= "Signup"
urlpatterns = [
     path('',signup,name='signup'),
      
]

