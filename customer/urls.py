from django.urls import path

from .views import wishlist,checkout,PlaceOrder

app_name = 'customer'

urlpatterns = [
    path('wishlist/', wishlist, name='wishlist'),
    path('checkout/', checkout, name='checkout'),
    path('place_order/', PlaceOrder.as_view(), name='place_order'),
]
