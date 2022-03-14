from django.shortcuts import render

# Create your views here.
from django.views import View


class HomePage(View):

    def get(self, request):
        return render(request, 'product/index.html', {})

class ContactPage(View):

    def get(self, request):
        return render(request, 'home/contact.html', {})

class AboutPage(View):

    def get(self, request):
        return render(request, 'home/about.html', {})
