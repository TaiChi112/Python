from django.shortcuts import render, redirect
from .mock import product_mock
from .models import Product, Cart, CartItem
from django.shortcuts import get_object_or_404


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

def cart_view(request):
     if request.user.is_authenticated:
        # ถ้า user มี cart แล้ว ให้ดึงมาใช้ แต่ถ้าไม่มีให้สร้างใหม่
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
     else:
        cart_items = []  # กรณีที่ผู้ใช้ยังไม่ล็อกอิน

     total_price = sum(item.get_total_price() for item in cart_items)

     context = {
        'cart_items': cart_items,
        'total_price': total_price,
     }
     return render(request, 'cart/cart.html',context)

def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')