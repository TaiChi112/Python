from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')
    
def about(request):
    return render(request, 'pages/about.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    
    context = {
        'sign_up': form
    }
    return render(request, 'account/sign_up.html',context)

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = SignInForm()

    context = {
        'sign_in': form}
    return render(request, 'account/sign_in.html',context)

def sign_out(request):
    logout(request)
    return redirect('index')

def profile(request):
    return render(request, 'account/profile.html')