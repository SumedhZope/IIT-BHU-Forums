from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

def home(request, *args, **kwargs):
    return render(request,'home.html',{'user' : request.user})
