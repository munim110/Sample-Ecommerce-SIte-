from unittest import result
from colorama import Cursor
from django.shortcuts import redirect, render
from Product.models import *
from django.db import connection

# Create your views here.

def home(request):
    if request.method == 'POST':
        string = request.POST.get('search')
        return redirect(search_view, string=string)
    else:
        all_products = Product.objects.all()
        print('Hello')
        return render(request, 'Home/home.html', {'all_products': all_products})

def search_view(request,string):
    if string is not None and string != '':
        all_products = Product.objects.filter(name__contains=string)
    else:
        all_products = Product.objects.all()
    return render(request, 'Home/search_result.html', {'all_products': all_products})