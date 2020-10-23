from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate,login
from .models import Group,Post,Comments
import datetime
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.http import HttpResponse,JsonResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



def nav(request):
    return render(request,'base_navbar.html')


def submit_form(request):
    def checkextenstion(s):
        allextension =[".jpg", '.jpeg', '.jpe','.jif', '.jfif', '.jfi',  '.png', '.gif' ,'.webp' , '.tiff', '.tif' , '.psd' , '.raw', '.arw', '.cr2', '.nrw', '.k25' ,'.bmp', '.dib' ,'.heif', '.heic' ,'.ind', '.indd', '.indt' ,'.jp2', '.j2k','.jpf', '.jpx', '.jpm', '.mj2', '.svg', '.svgz' ,'.ai','.eps']
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
        elif len(description)>120 :
            data ={
                'result' : 'error',
                'target' : 'Group Description',
                'message' : 'Group discription has a limitation 120 characters',
            }
            return JsonResponse(data)
        elif checkextenstion(g_icon.name):
            data ={
                'result' : 'error',
                'target' : 'Group Icon',
                'message' : 'Group Icon must be a Image file',
            }
            return JsonResponse(data)
        elif name is not None and description is not None:
            r = Group(name=name,description=description,groupicon= g_icon,created_at=now, user=request.user)
            r.save()
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
    if request.method == 'POST':
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
        
    post = Post.objects.get(id=kwargs.get('id'))
    comments = Comments.objects.filter(post=kwargs.get('id')).order_by('-created_at')
    for comment in comments:
        print(comment.created_at)
    context = {
        'post' : post,
        'comments' : comments,
    }
    return render(request, 'post_view.html', context)
  
def groups(request):
    group=Group.objects.all()
    params = {
        'group' : group
    }
    return render(request,'groups_landing.html',params)
  
def profile(request):
    return render(request,'profile.html')

