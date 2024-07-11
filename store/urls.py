from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('list/', views.listing, name="list"),
    path('product-detail', views.product_detail, name="product-detail"),
]
