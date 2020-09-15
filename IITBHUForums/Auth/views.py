from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .forms import CreateNewUserForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

#def loginpage(request, *args, **kwargs):
#    if(request.user.is_authenticated):
#        return redirect('/')
#    if request.method == "POST":
#        username = request.POST.get('username')
#        password = request.POST.get('password')
#        user = authenticate(request, username=username, password=password)
#        if user is not None:
#            login(request, user)
#            return redirect('/')
#        else:
#            print("Error")
#            return render(request, 'login.html')
#    return render(request, 'login.html')
#
#
#def register(request, *args, **kwargs):
#    if(request.user.is_authenticated) :
#        return redirect('/')
#    form = CreateNewUserForm()
#    if request.method == "POST":
#        form = CreateNewUserForm(request.POST)
#        if form.is_valid():
#            form.save()
#            username = request.POST.get('username')
#            password = request.POST.get('password1')
#            user = authenticate(request, username=username, password=password)
#            login(request, user)
#            return redirect('/')
#        else:
#            print("Error")
#            return render(request, 'register.html', {'form' : form})
#    return render(request, 'register.html', {'form' : form})

def landingpage(request,*args,**kwargs):
    if request.method == 'POST':
        if request.POST['btn'] == 'register':
            username = request.POST['username_signup']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            print(username,email,password1,password2)
            if password2 == password1:
                user = User.objects.create_user(username,email,password1)
                user = authenticate(request, username=username, password=password1)
                login(request,user)
            return HttpResponse('')
        elif request.POST['btn'] == 'login':
            username = request.POST['username_signin']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(reverse('navbar'))
            else:
                raise ValidationError("kya be? yeda hain kya?")
                return redirect(reverse('homepage'))
    else:
        return render(request, 'home.html')

def logout_func(request, *args, **kwargs):
    logout(request)
    return redirect(reverse('homepage'))




