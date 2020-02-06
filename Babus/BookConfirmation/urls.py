
from django.urls import path
from .views import buy,confirm_ticket


app_name= "Buy"
urlpatterns = [
     path('',buy,name='buy'),
     path('success',confirm_ticket,name='success'),
    #  path('generatePdf',toPdf,name='pdf'),
    
      
]

