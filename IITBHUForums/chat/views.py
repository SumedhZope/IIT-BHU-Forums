from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseForbidden,JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormMixin
from django.views.generic import DetailView, ListView
from .forms import ComposeForm
from .models import Thread, ChatMessage
from django.contrib.auth.models import User


def ThreadView(request,*args,**kwargs):
    other_username  = kwargs.get("username")
    obj, created    = Thread.objects.get_or_new(request.user, other_username)
    request.session['id'] = User.objects.get(username=other_username).id
    if obj == None:
        raise Http404
    return redirect("chatroom")
  
def chatroom(request):
    list_of_users = []
    for x in Thread.objects.by_user(request.user):
        if x.first != request.user:
            list_of_users.append([x.first,Thread.objects.get_or_new(x.first,x.second)[0]])
        else:
            list_of_users.append([x.second,Thread.objects.get_or_new(x.first,x.second)[0]])
    if 'id' in request.session.keys():
        return render(request,'chatroom.html', {'list' : list_of_users, 'id' : request.session['id'], 'username' : User.objects.get(id=request.session['id']).username})
    if len(list_of_users) > 0:
        return render(request,'chatroom.html', {'list' : list_of_users, 'id' : list_of_users[0][0].id, 'username' : list_of_users[0][0].username})
    else:
        return render(request,'chatroom.html', {'list' : list_of_users})
    return render(request,'chatroom.html', {'list' : list_of_users})
