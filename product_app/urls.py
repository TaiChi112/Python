from . import views
from django.urls import path

urlpatterns = [
    path('', views.Product_view, name='product')
]