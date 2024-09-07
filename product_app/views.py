from django.shortcuts import render
from .mock import product_mock
from .models import Product

# Create your views here.

def products_view(request):
    try:
        products = Product.objects.all()
    except Exception as e:
        products = product_mock
    
    context = {
        'products': products
    }
    return render(request, 'product/products.html', context)

def product_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Exception as e:
        product = product_mock
    context = {
        'product': product
    }
    return render(request, 'product/product.html', context)
