from django.shortcuts import render
from .mock import product_mock

# Create your views here.

def Product_view(request):
    context = {
        'products': product_mock
    }
    return render(request, 'product/products.html', context)