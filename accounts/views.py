from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            if password1 != password2:
                messages.error(request, "The two password fields didn't match")
            elif User.objects.filter(username=username).exists():
                messages.error(request, "A user with that username already exists")
            elif len(password1) < 8:
                messages.error(request, "This password is too short. It must contain at least 8 characters")
            elif not email:
                messages.error(request, "Enter a valid email address")
            else:
                User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                messages.success(request, "Registration successful. You can now log in.")
                return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Ensure this points to your dashboard or home page
            else:
                messages.error(request, "Username or password is invalid")
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
