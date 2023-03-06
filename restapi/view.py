from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')


def SignupPage(request):
    # if request.method == 'POST':
    #     uname = request.POST.get('username')
    #     email = request.POST.get('email')
    #     petname = request.POST.get('petname')
    #     pass1 = request.POST.get('password1')
    #     my_user = User.objects.create_user(uname, email,petname, pass1)
    #     return redirect('login')
    return render(request, 'signup.html')

def LoginPage(request):
    # username = request.POST.get('username')
    # pass1 = request.POST.get('pass')
    # user = authenticate(request, username=username, password=pass1)
    # if user is not None:
    #     login(request, user)
    #     return redirect('home')
    # else:
    #     return HttpResponse("Username or Password is incorrect!!!")


    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

def resetpassword(request):
    return render(request, 'resetpassword.html')

def Updatepassword(request):
    return render(request, 'Updatepassword.html')

