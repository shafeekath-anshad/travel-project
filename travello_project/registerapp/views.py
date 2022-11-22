from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        conpwd = request.POST['conpwd']
        if password == conpwd:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email,
                                                password=password)
                user.save()
                return redirect('login')
            messages.info(request, 'registered successfully')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('userpage')
        else:
            messages.info(request, "invalid login")
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def userpage(request):
    return render(request, "userpage.html")
