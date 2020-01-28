from django.shortcuts import render

# Create your views here.
@csrf_protect
def login(request):
    return render(request,'Login/login.html')


