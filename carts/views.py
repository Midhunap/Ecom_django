from django import http
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from . models import Cart, CartItem, Product


# Create your views here.

#to get the session id of cart
def _cart_id(request):     #private function
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart     

def add_cart(request,product_id):# also pass the product
    product = Product.objects.get(id = product_id) #get the product by id
    try:
        cart = Cart.objects.get(cart_id =_cart_id(request))#get the cart id using the cart id present in session
    except Cart.DoesNotExist:
        cart = Cart.objects.create( cart_id =_cart_id(request)) #create a new cart id if it doesnot exist in the cart
    cart.save()
    try:#product to inside a cart, products become cart
        cart_item = CartItem.objects.get(product = product ,cart = cart)
        cart_item.quantity += 1 #cart_item = cart_item + 1
        cart_item.save()
        
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    return HttpResponse(cart_item.quantity)  
    exit()  
    return redirect('cart')    


def cart(request):
    return render(request,'store/cart.html')