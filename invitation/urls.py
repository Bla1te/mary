from django.contrib import admin
from django.urls import path, re_path
from invitation import views

urlpatterns = [
    path("/<str:num>", views.index)
]
