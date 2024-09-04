from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, SignUpForm
from .models import CustomUser
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import login

# Create your views here.

def home(request):
    return render(request, 'general_app/home.html')

def about(request):
    return render(request, 'general_app/about.html')
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def user_login(request):  
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email'] 
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password) 
            if user:
                auth_login(request, user)
                next_url = request.POST.get('next')  
                if next_url:
                    return redirect(next_url)  
                return redirect('/')  
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):   
    auth_logout(request)  
    return redirect('/') 

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


# Test use case everything is custom

def sign_up(request):
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
    else:
        form = SignUpForm()
        
    context = {'form': form}
    return render(request, 'test/sign_up.html', context)

def sign_in(request):
    if request.method == "POST":
        form = SignInIUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignInIUser()
    
    context = {'form': form}
    return render(request, 'test/sign_in.html', context)