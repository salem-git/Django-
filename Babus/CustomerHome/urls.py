
from django.urls import path
from .views import  logged,cutomer_reserve_submission,fetch_journey,recent_journey_detail,buyTicket,confirm_ticket


app_name= "CustomerHome"
urlpatterns = [
     path('',logged,name='CustomerHome'),
     path('cutomer_reserve_submission',cutomer_reserve_submission,name='cutomer_reserve_submission'),
     path('buyTicket',buyTicket,name='buyTicket'),
     path('confirm_ticket',confirm_ticket,name='success'),
     path('recentJourney',fetch_journey,name='fetch_journey'),
     path('<int:rjourney_id>/',recent_journey_detail,name='recent_journey_detail'),


]

