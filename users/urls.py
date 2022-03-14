from django.urls import path

from .views import user_account, user_login, user_register

app_name = 'user'

urlpatterns = [
    path('', user_account, name='user_account'),
    path('login/', user_login, name='user_login'),
    path('register/', user_register, name='register'),
]
