from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    context = {
                'error': False,
            }
    

        


    return render(request,'main/login.html')