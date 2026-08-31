from django.shortcuts import render
from django.shortcuts import HttpResponse


def homepage(request):
    return HttpResponse("Welcome to django!")
