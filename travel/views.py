from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination, Demo


# Create your views here.
def travel(request):
    
    list_of_destinations = Destination.objects.all()
    
    
    
    demo=Demo.objects.filter(dest=4)
    if len(demo)>0:
        print(demo[0].author)
    return render(request,'index.html',{'dest':list_of_destinations})