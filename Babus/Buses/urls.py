
from django.urls import path
from .views import buses  


app_name= "Buses"
urlpatterns = [
     path('',buses,name='buses'),
      
]

