from django.shortcuts import render
from Product.models import *

# Create your views here.

def home(request):
    all_products = Product.objects.all()
    return render(request, 'Home/home.html', {'all_products': all_products})