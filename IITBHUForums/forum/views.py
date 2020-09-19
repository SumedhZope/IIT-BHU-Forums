from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

def nav(request):
    return render(request,'base_navbar.html')
def profile(request):
    return render(request,'profile.html')