from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

# 首頁
@login_required(login_url="Login")
def index(request):
    return render(request, 'accounts/index.html')

# 註冊
def sign_up(request):
    form = RegisterForm()
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/login')

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

# 登入
def sign_in(request):
    form = LoginForm()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')


    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def log_out(request):
    logout(request)
    return redirect('/login')

