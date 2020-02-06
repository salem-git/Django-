from django.shortcuts import render

# Create your views here.

def buy(request):
    return render(request,'BookConfirmation/buy.html')
def confirm_ticket(request):
    return render(request,'BookConfirmation/success.html')