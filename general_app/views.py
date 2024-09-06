from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')
    
def about(request):
    return render(request, 'pages/about.html')

def sign_in(request):
    return render(request, 'pages/sign_in.html')