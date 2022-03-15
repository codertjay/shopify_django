from django.urls import path

from .views import wishlist, Checkout

app_name = 'customer'

urlpatterns = [
    path('wishlist/', wishlist, name='wishlist'),
    path('checkout/', Checkout.as_view(), name='checkout'),
]
