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
    return render(request, 'Cart/viewcart.html',{'products':all_products,
    'totalPrice':cart.get_total_price(),'user':request.user})

def order(request):
    if request.method == 'POST':
        order = Order.objects.create(user=request.user)
        cart = Cart.objects.get(user=request.user)
        order.product.set(cart.product.all())
        order.shipping_address = request.POST['shipping_address']
        order.zip_code = request.POST['zip_code']
        order.shipping_city = request.POST['shipping_city']
        order.shipping_district = request.POST['shipping_district']
        order.shipping_division = request.POST['shipping_division']
        order.phone_number = request.POST['phone_number']
        order.email = request.user.email
        order.save()
        cart.product.clear()
        return render(request,'Cart/orderConfirmed.html',{'order':order})
    else:
        return render(request,'Cart/order.html',{'cart':Cart.objects.get(user=request.user),
        'all_products':list(Cart.objects.get(user=request.user).product.all()),
        'totalPrice':Cart.objects.get(user=request.user).get_total_price()})
