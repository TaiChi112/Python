from . import views
from django.urls import path

urlpatterns = [
    path('', views.products_view, name='products'),
    path('<int:id>/', views.product_view, name='product'),
]