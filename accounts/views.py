from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    PasswordChangeForm,
)
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model

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
    return redirect('accounts:login')


def profile(request,username):
    # 1. 현재 요청을 보낸 유저가 보고자하는 유저를 가져오기
    User = get_user_model() #User 모델 == 클래스
    profile_user = User.objects.get(username=username)
    
    context = {
        'profile_user' : profile_user,
    }
    return render(request, 'accounts/profile.html', context)    

