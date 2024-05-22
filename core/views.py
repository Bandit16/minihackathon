from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Profile


def homepage(request):
    # Create a new user

    return render(request, 'home.html')
