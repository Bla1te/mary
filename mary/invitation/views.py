from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(reques, num):
    return HttpResponse("<H1>page"+str(num)+"</H1>")