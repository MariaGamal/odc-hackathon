from django.core.checks import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth, messages


def login(request):
    return render(
        request=request,
        template_name='authentication/login.html'
    )


def register(request):
    return render(
        request=request,
        template_name='authentication/signup.html'
    )
