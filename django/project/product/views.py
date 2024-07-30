from django.shortcuts import render
from .mock import all_products 

# Create your views here.


def products(request):
    context = {
        'products': all_products
    }
    # return HttpResponse("Product List")
    return render(request, 'product/products.html', context)

def product(request,id):
    one_product = None
    try:
        one_product = [product for product in all_products if product['id'] == id][0]
    except IndexError:
        print("Product not found")
    context = {
        'product': one_product
    }
    # return HttpResponse("Product id : " + str(id)) 
    return render(request,"product/product.html",context)