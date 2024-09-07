from . import views
from django.urls import path

urlpatterns = [
    path('', views.products_view, name='products'),
    path('<int:id>/', views.product_view, name='product'),
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
]