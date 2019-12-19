from django.shortcuts import render
from .models import Bus

# Create your views here.

def buses(request):
    all_buses = Bus.objects.all()
    context = {'all_buses':all_buses}
    return render(request,"Buses/buses.html",context)
