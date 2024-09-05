from django.shortcuts import render

# Create your views here.

def Product_view(request):
    return render(request, 'product.html')