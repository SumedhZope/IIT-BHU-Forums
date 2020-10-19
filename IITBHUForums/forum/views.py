from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .models import Group,Post
import datetime
from django.contrib.auth.models import User

def nav(request):
    return render(request,'base_navbar.html')

def submit_form(request):
    name = request.POST.get("groupName")
    now = datetime.datetime.now()
    description = request.POST.get("Description")
    if name is not None and description is not None:
        r = Group(name=name,description=description,created_at=now, user=request.user)
        r.save()
    return render( request, "create_groups.html") 

def make_post(request):
    context = {
        'groups' : request.user.group_set.all()
    }        
    if request.method == 'POST':
        now = datetime.datetime.now()
        title = request.POST['title']
        content = request.POST['content']
        user = request.user
        group = Group.objects.get(id=request.POST['group'])

        if title is not None and content is not None :
            r = Post(title=title, content=content, created_at=now, user=user, group=group) 
            r.save()
    return render(request, 'make_post.html', context)
def groups(request):
    return render(request,'groups_landing.html')