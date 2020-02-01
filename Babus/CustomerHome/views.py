from django.shortcuts import render

# Create your views here.
def logged(request):
    return render(request,'CustomerHome/CustomerHome.html')