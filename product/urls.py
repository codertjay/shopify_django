from django.urls import path

from product.views import  products, product_detail

app_name = 'product'

urlpatterns = [
    path('products/', products, name='products'),
    path('detail/<str:slug>/', product_detail, name='product_detail')
]
