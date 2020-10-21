from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from Auth.models import userprofile
from .models import Group,Post
from django.http import HttpResponse

def feed(request):
    user = userprofile.objects.get(user=request.user)
    for g in Group.objects.all():
        g.members.add(user)
    post_list = []
    for g in user.group_set.all():
        for p in g.post_set.all():
            post_list.append(p)
            print(p.created_at)

    def get_created_date(Post):
        return Post.created_at
    post_list.sort(key=get_created_date, reverse=True)
    context = {
        'posts' : post_list
    }
    return render(request, 'feed.html', context)

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