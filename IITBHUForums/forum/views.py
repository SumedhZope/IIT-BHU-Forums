from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from Auth.models import Profile,Relationship,FriendRequest
from .models import Group,Post,like
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Group,Post,Comments,Role, Role_choices
import datetime
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.http import HttpResponse,JsonResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from PIL import Image
from Auth.models import Profile
from django.core.exceptions import PermissionDenied

def feed(request):
    user = Profile.objects.get(user=request.user)

    for g in Group.objects.all(): #to be removed, when joining of group feature is added, done just for testing
        g.members.add(user)

    post_list = []
    
    for g in user.group_set.all():
        for p in g.post_set.all():
            post_list.append(p)
            
    def get_created_date(Post):
        return Post.created_at
    post_list.sort(key=get_created_date, reverse=True)
    context = {
        'posts' : post_list
    }
    return render(request, 'feed.html', context)

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

    is_friend = ""

    if Profile.objects.get(user=request.user) in friends or request.user == u:
        is_friend = "True"
    else:
        is_friend = "False"

    context={
        'u' : u,
        'button_status' : button_status,
        'friends_list' : friends,
        'sent_friend_requests' : sent_friend_requests,
        'rec_friend_requests' : rec_friend_requests,
        'groups' : u.group_set.all(),
        'posts' : u.post_set.all(),
        'friends' : friends,
        'is_friend' : is_friend,
    }
    return render(request,'profile.html',context)
            

def friend_request(request, *args, **kwargs):
    requests = FriendRequest.objects.filter(to_user = request.user)
    context = {
        'requests' : requests
    }
    return render(request,'friend_requests.html',context)

def add_member(request, *args, **kwargs):
    group = Group.objects.get(id=1) 
    group.members.add(Profile.objects.get(user=request.user))
    return HttpResponse("<h1> Done! <h1>")

def member_list(request,*args,**kwargs):
    group = Group.objects.get(id=kwargs.get('id'))
    member = [[person.user.username, Role.objects.filter(group=group).get(user=person.user).role, person.user.id] for person in group.members.all()]
    if Role.objects.filter(group=group).get(user=request.user).role == "Admin":
        isadmin = "True"
    else:
        isadmin = "False"
    context = {
        'member' : member,
        'check_admin' : isadmin,
        'group' : group,
        'role_choices' : Role_choices.objects.filter(group=group)
    }
    if request.method == "POST":
        r = Role.objects.get(user=User.objects.get(id=request.POST.get('user_id')), group=group)
        r.role = request.POST.get('new_role')
        r.save()
    return render(request, 'member.html',  context)

def search(request):
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

def submit_form(request):
    def checkextenstion(s):
        allextension =[".jpg", '.jpeg', '.jpe','.jif', '.jfif', '.jfi',  '.png', '.gif' ,'.webp' , '.tiff', '.tif' , '.psd' , '.raw', '.arw', '.cr2', '.nrw', '.k25' ,'.bmp', '.dib' ,'.heif', '.heic' ,'.ind', '.indd', '.indt' ,'.jp2', '.j2k','.jpf', '.jpx', '.jpm', '.mj2', '.svg', '.svgz' ,'.ai','.eps','.html']
        for xtenstion in allextension:
            if s.endswith(xtenstion):
                return False
        return True
    if request.method=='POST' :
        name = request.POST.get("groupName")
        now = datetime.datetime.now()
        description = request.POST.get("Description")
        g_icon = request.FILES['groupicon']
        name = name.strip()
        description = description.strip()
        if len(name)>50 or len(name)<3:
            data = {
                'result' : 'error',
                'target' : 'Group Name',
                'message' : 'Group name had a length limitation of 3 to 50 characters',
            }
            return JsonResponse(data)
        elif len(description)>120 or len(description)<3:
            data ={
                'result' : 'error',
                'target' : 'Group Description',
                'message' : 'Group description has a limitation 120 characters',
            }
            return JsonResponse(data)
        elif checkextenstion(g_icon.name) and g_icon.name is not None:
            data ={
                'result' : 'error',
                'target' : 'Group Icon',
                'message' : 'Group Icon must be a Image file',
            }
            return JsonResponse(data)
        elif name is not None and description is not None:
            r = Group(name=name,description=description,groupicon= g_icon,created_at=now, user=request.user,likes=0)
            r.save()
            request.user.profile.group_set.add(r)
            n = Role(user=request.user, group=r, role="Admin")
            n.save()
            n = Role_choices(group=r, role="Admin")
            n.save()
            n = Role_choices(group=r, role="Member")
            n.save()
            data = {
                'result' : 'success',
            }
            return JsonResponse(data)
    return render(request, "create_groups.html") 

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
            return redirect(reverse('post_view',kwargs={
                    'id' : r.id
                }))
    return render(request, 'make_post.html', context)

def post_view(request,*args,**kwargs):
    print(request.POST)
    if request.method == 'POST':
        if request.POST.get('comment'):
            now = datetime.datetime.now()
            comment = request.POST['comment']
            if comment is not None :
                post = Post.objects.get(id=kwargs.get('id'))
                c = Comments(user=request.user, comment=comment, created_at=now, post=post)
                c.save()
                data = {
                    'result' : 'success',
                    'new_comment' : comment,
                    'user' : request.user.username,
                    'date' : now
                }
                return JsonResponse(data)
            data = {
                'result' : 'fail',
            }
            return JsonResponse(data)

        if request.POST.get("like"):
            if request.POST.get("like") == "create":
                print("create")
                data = {
                    'result' : 'success',
                }
                new_like = like(user=request.user, post=Post.objects.get(id=kwargs.get('id')))
                new_like.save()
                print(like.objects.filter(user=request.user))
                return JsonResponse(data)
            else:
                print("delete")
                like_delete = like.objects.filter(post=Post.objects.get(id=kwargs.get('id')),user=request.user)
                like_delete.delete()
                data = {
                    'result' : 'success',
                }
                return JsonResponse(data)

    post = Post.objects.get(id=kwargs.get('id'))
    comments = Comments.objects.filter(post=kwargs.get('id')).order_by('-created_at')
    likes = like.objects.filter(post=post)

    status = 0
    if likes.filter(user=request.user):
        status = 1

    num_comments = comments.count()
    context = {
        'post' : post,
        'comments' : comments,
        'num' : num_comments,
        'num_likes' : likes.count(),
        'status_like' : status
    }
    return render(request, 'post_view.html', context)
  
def groups(request):
    group=Group.objects.all()
    params = {
        'group' : group
    }
    if request.method == "POST":
        Group.objects.get(id=request.POST.get('group_id')).members.add(request.user.profile)
        r = Role(user=request.user, group=Group.objects.get(id=request.POST.get('group_id')), role="Member")
        return render(request,'groups_landing.html',params)    
    return render(request,'groups_landing.html',params)
  
def group_home(request, id):
    group = Group.objects.get(id=id)
    if request.method == "POST":
        likes = int(request.POST.get('like'))
        print(likes)
        group.likes = likes
        if request.POST.get('val') == 'inc':
            group.liked_by.add(request.user)
        else :
            group.liked_by.remove(request.user)
        group.save()
    x = Group.objects.filter(liked_by=request.user,id = id)
    params ={}
    if x :
        params = {
        'group' : group,
        'liked' : True,
        }
    else :
        params = {
        'group' : group,
        'liked' : False,
        }
    return render(request,'group_home.html',params)

def add_role(request, *args, **kwargs):
    group = Group.objects.get(id=kwargs.get('id'))
    if Role.objects.filter(group=group).get(user=request.user).role != "Admin" :
        raise PermissionDenied
    else:
        context = {
            'existing_role' : Role_choices.objects.filter(group=group),
            'group' : group
        }
        if request.method == "POST":
            role_name = request.POST.get('role').strip()
            if role_name == '':
                data = {
                    'result' : 'error',
                    'message' : 'Role name not allowed' 
                }
                return JsonResponse(data)
            elif role_name.upper() in [role.role.upper() for role in Role_choices.objects.filter(group=group)]:
                data = {
                    'result' : 'error',
                    'message' : 'Role name already exists' 
                }
                return JsonResponse(data)
            else:
                r = Role_choices(group=group, role= request.POST.get('role'))
                r.save()
                data = {
                    'result' : 'success',
                    'message' : 'Role successfully added'
                }
                return JsonResponse(data)
            return render(request, 'add_role.html', context)    
        return render(request, 'add_role.html', context)