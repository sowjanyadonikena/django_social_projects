import social_django
from social_django import models, views

from django.shortcuts import render,redirect
from social_django.utils import load_strategy, load_backend
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    return render(request,'login.html')


@login_required
def home(request):
    return render(request,'home.html')
