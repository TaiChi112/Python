from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.index, name="index"),
    path("", views.home, name="home"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("sign_in/", views.sign_in, name="sign_in"),
    path("product_list/", views.product_list, name="product_list"),
    path("product_list/product_detail/", views.product_detail, name="product_detail"),
]
