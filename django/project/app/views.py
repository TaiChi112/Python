from django.shortcuts import render

# Create your views here.
def sign_up(request):
    return render(request, 'app/sign_up.html')

def sign_in(request):
    return render(request, 'app/sign_in.html')

def index(request):
    return render(request, "app/index.html")
def home(request):
    return render(request, "app/home.html")

def product_list(request):
    return render(request, "app/product_list.html")


def product_detail(request):
    return render(request, "app/product_detail.html")
