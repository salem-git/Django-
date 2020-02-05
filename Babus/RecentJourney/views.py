from django.shortcuts import render

# Create your views here.
def recentJourney(request):
    return render(request,'CustomerHome/recentJourney.html')