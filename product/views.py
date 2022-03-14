from django.shortcuts import render

# Create your views here.
from django.views import View




def products(request):
    return render(request, 'product/list.html')


def product_detail(request, slug=None):
    return render(request, 'product/detail.html')

