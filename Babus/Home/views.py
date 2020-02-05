from django.shortcuts import render
from django.http import HttpResponse
from Buses.models import Bus

# Create your views here.

def home(request):
    return render(request,'Home/index.html')


def search(request):
    qs = Bus.objects.all()
    
    lo_search = request.GET.get('lo-search')
    

    if lo_search != '' and lo_search is not None:
        qs = qs.filter(name=lo_search)

    context = {
        'queryset':qs
    }
    return render(request,"Home/searchResult.html",context)
