from django.shortcuts import render



def products(request):
    return render(request, 'product/list.html')


def product_detail(request, slug=None):
    return render(request, 'product/detail.html')

