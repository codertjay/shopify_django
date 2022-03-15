from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View


def wishlist(request):
    return render(request, 'customer/wish_list.html')


class Checkout(View):
    def get(self, request):
        return render(request, 'customer/checkout.html',
                      {'stripe_public_key': 'pk_test_0kwoXbmhxUvOxN00BSkLynRe00ZnQxtpJk'})

    def post(self, request):
        messages.success(request, 'Order was successful')
        return redirect('customer:checkout')
