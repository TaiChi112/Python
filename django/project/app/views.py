from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'app/index.html')

def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
    return render(request,'app/sign_in.html')

def product_list(request):
    return render(request,'app/product_list.html')

def product_detail(request):
    return render(request,'app/product_detail.html')
