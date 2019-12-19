from django.shortcuts import render,redirect
from .forms import UserRegistration

# Create your views here.

# def signup(request):
#     return render(request,'Signup/index.html')

def signup(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = UserRegistration() 
    context = {'form':form}
    return render(request,'Signup/index.html',context)
