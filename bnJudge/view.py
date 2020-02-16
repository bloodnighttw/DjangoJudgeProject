from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import auth, User
from repo import repos


def index(request):
    return render(request, "index.html" ,{ 'repo': repos.repos })


