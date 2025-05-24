from . import views
from django.urls import path

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:tour_id>/', views.add_to_cart, name='add_to_cart'),
    path('booking/', views.checkout_view, name='booking'),
    path('confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    ]