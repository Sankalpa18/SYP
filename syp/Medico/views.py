from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def Home(request):
    return render(request,'HomePage.html',{})

def Signup(request):
    if request.method=='POST':
        username=request.POST.get('gmail')
        password=request.POST.get('password')
        confirmation=request.POST.get('confirm')
        
        if password==confirmation:
            MedicoUser= User.objects.create_user(username, password, confirmation)
            MedicoUser.save()
            return redirect('login')
        else:
            return HttpResponse("Two different password")
    
    return render(request,'Register.html',{})

def Login(request):
    if request.method=='POST':
        username=request.POST.get('gmail')
        password=request.POST.get('password')
        MedicoUser=authenticate(request, username=username, password=password)
        if MedicoUser is not None:
            login(request, MedicoUser)
            return redirect('Home')
        else:
            return HttpResponse("different password")

    return render(request,'Login.html',{})
