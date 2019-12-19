from django.shortcuts import render

# Create your views here.

def buses(request):
    return render(request,"Buses/buses.html")
