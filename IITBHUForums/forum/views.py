from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from Auth.models import userprofile,Relationship
from .models import Group,Post
from django.http import HttpResponse,JsonResponse

def nav(request):
    return render(request,'base_navbar.html')

def profile(request, *args, **kwargs):
    if request.method == 'POST':
        user = userprofile.objects.get(user=User.objects.get(id=kwargs.get('id')))
        user.friend.add(userprofile.objects.get(user=request.user))
        data = {
           'result' : 'success',
        }
        return JsonResponse(data)
    user = User.objects.get(id=kwargs.get('id'))
    user_profile = userprofile.objects.get(user=user)
    profile = userprofile.objects.get(user=request.user)

    context = {
        'user' : user,
        'status' : 1,
    }
    is_friend = userprofile.objects.filter(friend=profile.id)
    print(is_friend)
    #if friends[user.username]:
    #    context['status'] = 2
    return render(request,'profile.html',context)

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