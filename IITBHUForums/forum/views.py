from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from Auth.models import userprofile
from .models import Group,Post
from django.http import HttpResponse

def nav(request):
    return render(request,'base_navbar.html')

def profile(request):
    return render(request,'profile.html')

def add_member(request, *args, **kwargs):
    group = Group.objects.get(id=1) #add group here
    group.members.add(userprofile.objects.get(user=request.user))
    return HttpResponse("<h1> Done! <h1>")
def group_list(request,*args,**kwargs):
    group = Group.objects.get(id=kwargs.get('id'))
    group.members.add(userprofile.objects.get(id=1))
    context = {
        'member' : group.members.all()
    }
    return render(request, 'member.html',  context)