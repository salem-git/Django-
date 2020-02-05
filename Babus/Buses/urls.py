
from django.urls import path
from .views import buses,toPdf,detail


app_name= "Buses"
urlpatterns = [
     path('',buses,name='buses'),
     path('generatePdf',toPdf,name='pdf'),
     path('<int:bus_id>/',detail,name='detail'),
      
]

