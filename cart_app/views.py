from django.shortcuts import render,redirect,get_object_or_404
from plant_app.models import *
from.models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
   

def cartproducts(request,tot=0,count=0,cart_item=None):
    try:
        cart=CartList.objects.get(cart_id=c_id(request))
        cart_item=CartItems.objects.filter(cart=cart)
        for i in cart_item:
            tot +=(i.product.price * i.quantity)
            count +=i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'cartitem':cart_item,'total':tot,'count':count})     
       
def c_id(request):
    cart_id=request.session.session_key
    if not cart_id:
        cart_id=request.session.create()
    return cart_id


def addcart(request,product_id):
    product=Products.objects.get(id=product_id)
    try:
        cart=CartList.objects.get(cart_id=c_id(request))
    except CartList.DoesNotExist:
        cart=CartList.objects.create(cart_id=c_id(request))
        cart.save()
    try:
        cart_item=CartItems.objects.get(product=product,cart=cart)
        if cart_item.quantity<cart_item.product.stock:
            cart_item.quantity += 1
            cart_item.save()
    except CartItems.DoesNotExist:
        cart_item=CartItems.objects.create(product=product,quantity=1,cart=cart)
        cart_item.save()
    return redirect('cartdet')    


def dicrement(request,product_id):
    cart=CartList.objects.get(cart_id=c_id(request))
    product=get_object_or_404(Products,id=product_id)
    cart_items=CartItems.objects.get(product=product,cart=cart)
    if cart_items.quantity >1:
        cart_items.quantity -=1
        cart_items.save()
    else:
        cart_items.delete()
    return redirect('cartdet')

def delete(request,product_id):
    cart=CartList.objects.get(cart_id=c_id(request))
    product=get_object_or_404(Products,id=product_id)
    cart_items=CartItems.objects.get(product=product,cart=cart)
    cart_items.delete()
    return redirect('cartdet')

