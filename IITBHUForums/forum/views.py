from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from Auth.models import Profile,Relationship,FriendRequest
from .models import Group,Post
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

def nav(request):
    return render(request,'base_navbar.html')

def send_friend_request(request, *args, **kwargs):
   # print(request.user.is_authenticated())
    if request.user.is_authenticated:
    #    print(1)
        user = get_object_or_404(User,id=kwargs.get('id'))
        frequest, created = FriendRequest.objects.get_or_create(
            from_user=request.user,
            to_user=user
        )
        data = {
           'result' : 'success',
        }
        return JsonResponse(data)

def cancel_friend_request(request,id):
    if request.user.is_authenticated():
        user = get_object_or_404(User,id=id)
        frequest = FriendRequest.objects.filter(
            from_user=request.user,
            to_user=user
        ).first()
        frequest.delete()
        return HttpResponseRedirect()

def accept_friend_request(request, *args, **kwargs):
    from_user = get_object_or_404(User,id=kwargs.get('id'))
    frequest = FriendRequest.objects.filter(from_user=from_user,to_user=request.user).first()
    user1 = frequest.to_user
    user2 = from_user
    user1 = Profile.objects.get(user=user1)
    user2 = Profile.objects.get(user=user2)
    user1.friends.add(user2)
    user2.friends.add(user1)
    frequest.delete()
    data = {
        'result' : 'success',
    }
    return JsonResponse(data)
    #return HttpResponseRedirect('user/{}'.format(request.user.Profile.slug))

def delete_friend_request(request, *args, **kwargs):
    from_user = get_object_or_404(User, id=kwargs.get('id'))
    print(from_user)
    frequest = FriendRequest.objects.filter(from_user=from_user,to_user=request.user).first()
    frequest.delete()
    data = {
        'result' : 'success',
    }
    return JsonResponse(data)
    #return HttpResponseRedirect('user/{}'.format(request.user.Profile.slug))

def profile(request, *args, **kwargs):
    u = User.objects.get(id=kwargs.get('id'))
    p = Profile.objects.get(user=u)
    sent_friend_requests = FriendRequest.objects.filter(from_user = p.user)
    rec_friend_requests = FriendRequest.objects.filter(to_user = p.user)

    friends = p.friends.all()

    #if user is friend
    button_status = 'you both are friends'
    if p not in Profile.objects.get(user=request.user).friends.all():
        button_status = 'not_friend'

        #if friend request is sent
        if len(FriendRequest.objects.filter(from_user = request.user).filter(to_user = p.user)) == 1:
            button_status = 'friend_request_sent'
        
        #if friend request is given
        if len(FriendRequest.objects.filter(from_user = p.user).filter(to_user = request.user)) == 1:
            button_status = 'friend_request'
    
    #if same user
    if u.id==request.user.id:
        button_status = 'own profile'

    context={
        'u' : u,
        'button_status' : button_status,
        'friends_list' : friends,
        'sent_friend_requests' : sent_friend_requests,
        'rec_friend_requests' : rec_friend_requests,
        'groups' : request.user.group_set.all(),
        'posts' : request.user.post_set.all(),
        'friends' : friends,
    }
    return render(request,'profile.html',context)
            

def friend_request(request, *args, **kwargs):
    requests = FriendRequest.objects.filter(to_user = request.user)
    context = {
        'requests' : requests
    }
    return render(request,'friend_requests.html',context)


#def profile(request, *args, **kwargs):
#    if request.method == 'POST':
#        user = userprofile.objects.get(user=User.objects.get(id=kwargs.get('id')))
#        user.friend.add(userprofile.objects.get(user=request.user))
#        data = {
#           'result' : 'success',
#        }
#        return JsonResponse(data)
#    user = User.objects.get(id=kwargs.get('id'))
#    user_profile = userprofile.objects.get(user=user)
#    profile = userprofile.objects.get(user=request.user)
#
#    context = {
#        'user' : user,
#        'status' : 1,
#    }
#    is_friend = userprofile.objects.filter(friend=profile.id)
#    print(is_friend)
#    #if friends[user.username]:
    #    context['status'] = 2
#    return render(request,'profile.html',context)

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