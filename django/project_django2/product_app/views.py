from django.shortcuts import render
from .mock import product_list

# Create your views here.

def products(request):
    return render(request, 'product_app/products.html',{'product_list': product_list})

def product_detail(request, id):
    product = next((prod for prod in product_list if prod['id'] == id), None)
    # print(product)
    context = {
        'product': product
    }
    # print(context)
    return render(request, 'product_app/product.html', context)