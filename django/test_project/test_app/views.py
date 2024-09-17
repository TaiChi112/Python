from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import CustomUser
# Create your views here.

# views.py
def home_view(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = CustomUser.create_user(
                email=form.cleaned_data['email'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = CustomUser.objects.get(email=email)
                if user.check_password(password):
                    request.session['user_id'] = user.id
                    messages.success(request, 'Login successful!')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid email or password')
            except CustomUser.DoesNotExist:
                messages.error(request, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
