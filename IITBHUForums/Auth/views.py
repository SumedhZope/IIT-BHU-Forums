from django.shortcuts import render,redirect
from .forms import CreateNewUserForm
from django.contrib.auth import authenticate,login

def loginpage(request, *args, **kwargs):
    if(request.user.is_authenticated):
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print("Error")
            return render(request, 'login.html')
    return render(request, 'login.html')


def register(request, *args, **kwargs):
    if(request.user.is_authenticated) :
        return redirect('/')
    form = CreateNewUserForm()
    if request.method == "POST":
        form = CreateNewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            print("Error")
            return render(request, 'register.html', {'form' : form})
    return render(request, 'register.html', {'form' : form})
