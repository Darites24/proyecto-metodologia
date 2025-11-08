from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('conversor:home')
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.cleaned_data['user']
        login(request, user)
        return redirect('conversor:home')
    return render(request, 'usuarios/login.html', {'form': form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('conversor:home')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        return redirect('usuarios:login')
    return render(request, 'usuarios/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('usuarios:login')    
