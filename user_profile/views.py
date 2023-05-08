from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import *
from .forms import *


# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            messages.success(request, 'Вы успешно зарегестрировались')
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('edit')
    else:
        form = RegisterForm()
    return render(request, 'user_profile/register.html', {'form': form})


def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ProfileForm()
    return render(request, 'user_profile/edit.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'user_profile/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')
