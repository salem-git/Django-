
from django.urls import path
from .views import home,search
from django.conf import settings
from django.conf.urls.static import static


app_name= "Home"
urlpatterns = [
     path('',home,name='index'),
     path('search',search,name='search'),
     
      
]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

