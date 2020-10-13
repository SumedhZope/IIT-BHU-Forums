from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .models import Group 
import datetime

def nav(request):
    return render(request,'base_navbar.html')
def submit_form(request):
    print (request.POST)
    name = request.POST.get("groupName")
    now = datetime.datetime.now()
    description = request.POST.get("Description")
    if name is not None and description is not None:
        r = Group(name=name,description=description,created_at=now)
        r.save()
    return render( request, "create_groups.html") 