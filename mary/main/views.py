from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.
def login(request):
    return render(request,'main/login.html')

def index(request):
    return render(request, 'main/main.html')

def logout_user(request):
    logout(request)
    return redirect('main')