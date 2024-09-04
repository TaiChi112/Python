from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .mock import products 
from .form import SignUpForm

# Create your views here.

def index(request):
    return render(request, "app/index.html")

def about(request):
    return render(request, "app/about.html")

def form(request):
    return render(request, "app/form.html")

# def sign_up(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('')
#     else:
#         form = SignUpForm()

#     return render(request, 'app/sign_up.html', {'form': form})

# def sign_in(request):
#     return render(request, 'app/sign_in.html')


# def profile(request):
#     return render(request, "app/profile.html")

# def product_list(request):
#     context = {
#         'products': products
#     }

#     return render(request, "app/product_list.html", context)


# def product_detail(request,id):

#     product = {
#         'id': id,
#         'name': 'Earthen Bottle',
#         'description': 'Tall slender porcelain bottle with natural clay textured body and cork stopper.',
#         'price': 112,
#         'image_url': 'https://tailwindui.com/img/ecommerce-images/category-page-04-image-card-01.jpg'
#     }

#     context = {
#         'product': product
#     }
#     return render(request, "app/product_detail.html", context)
    
# def profile(request):
#     return render(request, "app/profile.html")

# def test(request,id,name):
#     return render(request, "app/test.html", {"id": id, "name": name})