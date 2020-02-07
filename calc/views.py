from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("<html><body bgcolor='pink' top=300px left=400px >Hello World!</body></html>")
    return render(request,'home.html',{'name':'Rahul'})

def result(request):
    try:
        a=int(request.POST['val1'])
        b=int(request.POST['val2'])
        res=a+b
    except:
        res="Please Enter numbers !!"
    
    return render(request, 'result.html',{'result':res})

