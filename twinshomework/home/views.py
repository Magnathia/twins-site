from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name='home/homepage.html',
                  context={})


def wsu(request):
    return render(request=request,
                  template_name='home/Ethan_WSU.html',
                  context={})


def harvard(request):
    return render(request=request,
                  template_name='home/ethan_harvard.html',
                  context={})


def bellevue(request):
    return render(request=request,
                  template_name='home/eric_bellevue.html',
                  context={})

def about(request):
    return render(request=request,
                  template_name='home/about.html',
                  context={})


def caltech(request):
    return render(request=request,
                  template_name='home/eric_caltech.html',
                  context={})
