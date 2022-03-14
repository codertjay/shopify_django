from django.shortcuts import render


# Create your views here.


def user_account(request):
    return render(request, 'user/account.html')


def user_login(request):
    return render(request, 'user/login.html')


def user_register(request):
    return render(request, 'user/register.html')
