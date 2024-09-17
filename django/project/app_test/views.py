from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, 'app_test/test.html')

def about(request):
    return render(request, 'app_test/about.html')