from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    context = {
                'error': False,
            }
    if request.method == 'POST':
        username = request.POST.get('username')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            context['error'] = True
            #user = User.objects.create_user(username=username)
        auth_login(request, user)
        context['index'] = True
        return redirect("")

        


    return render(request,'main/login.html')