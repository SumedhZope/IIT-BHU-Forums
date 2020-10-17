from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Post, Group
from django.contrib.auth import authenticate,login

def feed(request):
    if request.GET:
        query = request.GET.get('q')
        group_list = Group.objects.filter(Q(name__icontains = query))
        post_list = Post.objects.filter(Q(title__icontains = query))
        user_list = User.objects.filter(Q(username__icontains = query))
        context = {
            'groups' : group_list,
            'posts' : post_list,
            'users' : user_list,
        }
        print(group_list,post_list,user_list)
        return render(request, 'search.html', context)
    return render(request, 'feed.html')

def nav(request):
    return render(request,'base_navbar.html')

def profile(request):
    return render(request,'profile.html')