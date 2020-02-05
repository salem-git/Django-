from django.shortcuts import render
from .models import Train

# Create your views here.

def train(request):
    all_trains = Train.objects.all()
    context = {'all_trains':all_trains}
    return render(request,"Train/train.html",context)
