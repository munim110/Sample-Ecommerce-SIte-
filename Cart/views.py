from django.shortcuts import render
from Users.models import *
from Cart.models import *

# Create your views here.

def view_cart(request,user_id):
    user = request.user
    try:
        userprofile = Userprofile.objects.get(user=user)
    except:
        userprofile = Userprofile.objects.create(user=user)
    cart = Cart.objects.get(user=user)
    all_products = list(cart.product.all())
    return render(request, 'Cart/viewcart.html',{'products':all_products,'totalPrice':cart.get_total_price()})
