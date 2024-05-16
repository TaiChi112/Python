from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_in/',views.sign_in,name='sign_in'),
    path('product_list/',views.product_list,name='product_list'),
    path('productList/productDetail/',views.product_detail,name='product_detail'),
]