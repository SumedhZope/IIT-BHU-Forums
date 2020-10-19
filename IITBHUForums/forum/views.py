from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate,login
from .models import Group,Post,Comments
import datetime

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
            c = Comments(comment=comment, created_at=now, post=post)
            c.save()
            data = {
                'result' : 'success',
                'new_comment' : comment,
            }
            return JsonResponse(data)
        data = {
            'result' : 'fail',
        }
        return JsonResponse(data)
        
    post = Post.objects.get(id=kwargs.get('id'))
    comments = Comments.objects.filter(post=kwargs.get('id'))
    context = {
        'post' : post,
        'comments' : comments,
    }
    return render(request, 'post_view.html', context)