from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    PasswordChangeForm,
)
from .forms import CustomUserChangeForm, CustomUserCreationForm


# Create your views here.

def login(request):
    if request.user.is_authenticated:
        pass
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            #pass
            return redirect('instargram:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }    
    return render(request, 'accounts/login.html', context)


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('instargram:index')
    else:
        form = CustomUserChangeForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('instargram:index')

