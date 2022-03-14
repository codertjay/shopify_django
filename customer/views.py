from django.shortcuts import render, redirect

# Create your views here.
from django.views import View


def wishlist(request):
    return render(request, 'customer/wish_list.html')


def checkout(request):
    return render(request, 'customer/checkout.html')


class PlaceOrder(View):
    def get(self, request):
        return render(request, 'customer/place_order.html', {'stripe_public_key': 'stripe_public_key'})

    def post(self, request):
        return redirect('customer:place_order')
