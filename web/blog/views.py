from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from . forms import RegisterForm
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'index.html' )

def login(request):
    if request.method == "POST":
        username= request.POST.get('from_username_email')
        password = request.POST.get('form_password')
        user=authenticate(request, username=username, password=password)

    return render(request, 'login.html')    


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            login (request, form)
        return redirect("/") #anything else I put here is returning something like this register/login.html instead of http://127.0.0.1:8000/login.html
    else:
        form = RegisterForm()
    context = {'form': form}
    
    return render(request, "register.html", context)