from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from .forms import CreateNewUserForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def landingpage(request,*args,**kwargs):
    if request.user.is_authenticated:
        return redirect(reverse("feed"))
    if request.method == 'POST':
        if request.POST['btn'] == 'register':
            username = request.POST['username_signup']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if len(username)>20:
                data = {
                    'result' : 'error',
                    'target' : 'username',
                    'message' : 'Username had a length limitation of 20 characters',
                }
                return JsonResponse(data)
            if User.objects.filter(username=username).exists()==False:
                if password2 == password1:
                    if len(password1)<8:
                        data = {
                            'result' : 'error',
                            'target' : 'password',
                            'message' : 'Password must contain atleast 8 characters',
                        }
                        return JsonResponse(data)
                    user = User.objects.create_user(username,email,password1)
                    user = authenticate(request, username=username, password=password1)
                    login(request,user)
                    data = {
                        'result' : 'success',
                    }
                    return JsonResponse(data)
                else:
                    data = {
                        'result' : 'error',
                        'target' : 'password',
                        'message' : 'Your password didn\'t match',
                    }
                    return JsonResponse(data)
            else:
                data = {
                    'result' : 'error',
                    'target' : 'username',
                    'message' : 'Username already taken',
                }
                return JsonResponse(data)
                
        elif request.POST['btn'] == 'login':
            username = request.POST['username_signin']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                data = {
                    'result' : 'success',
                }
                return JsonResponse(data)
            else:
                data = {
                    'result' : 'error',
                }
                return JsonResponse(data)
    else:
        return render(request, 'home.html')

def logout_func(request, *args, **kwargs):
    logout(request)
    return redirect(reverse('homepage'))
