from django.shortcuts import render
from .mock import product_list

# Create your views here.

def products(request):
    return render(request, 'product_app/products.html',{'product_list': product_list})

def product(request,data):
    return render(request, 'product_app/product.html',{'data':data})