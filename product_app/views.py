from django.shortcuts import render, redirect
from .mock import product_mock
from .models import Product, Cart, CartItem
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.

@login_required(login_url='sign_in')
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
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
     else:
        cart_items = []

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

    return redirect(request.META.get('HTTP_REFERER', 'index'))
 

def remove_from_cart(request, id):
    # ดึงข้อมูลสินค้า
    product = get_object_or_404(Product, id=id)

    # ตรวจสอบว่าผู้ใช้ล็อกอินหรือไม่
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
    
    # ค้นหา CartItem ที่ตรงกับสินค้านั้นๆ
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)

    # ถ้าจำนวนสินค้ามากกว่า 1 ให้ลดจำนวน
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        # ถ้าจำนวนสินค้าเหลือน้อยกว่าหรือเท่ากับ 0 ให้ลบออกจากตะกร้า
        cart_item.delete()

    # redirect กลับไปยังหน้าแสดงตะกร้า
    return redirect('cart')