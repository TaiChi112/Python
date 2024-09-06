from django.shortcuts import render
from .mock import product_mock
from .models import Product

# Create your views here.

def Product_view(request):
    # context = {
    #     'products': product_mock
    # }

    context = {
        'products': Product.objects.all()
    }
    return render(request, 'product/products.html', context)