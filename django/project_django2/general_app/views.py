from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'general_app/home.html')

def about(request):
    return render(request, 'general_app/about.html')