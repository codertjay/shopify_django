from django.urls import path

from .views import HomePage, ContactPage, AboutPage

app_name = 'home'

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),

    path('contact/', ContactPage.as_view(), name='contact'),
    path('about/', AboutPage.as_view(), name='about'),
]
