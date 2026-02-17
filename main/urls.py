from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as lviews
from main import views


urlpatterns = [
    path('login', lviews.LoginView.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
    path('', views.index, name='main'),

]
