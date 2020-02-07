from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        first= request.POST['first']
        last=request.POST['last']
        username=request.POST['user']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1==pass2:
            if User.objects.filter(username=username).exists() :
                messages.info(request,'Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists() :
                messages.info(request,'Email already taken')
                return redirect('register')
            else:
                user= User.objects.create_user(username=username,first_name=first,last_name=last,email=email,password=pass1)
                user.save()
                messages.info(request,'User Created Successfully')
                return redirect('/')
            
        else:
            

            messages.info(request,'Password did not match')
            return redirect('register')
        
        
    else:
    
        return render(request,'register.html',{'name':'Rahul'})