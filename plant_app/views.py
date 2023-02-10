from django.shortcuts import render
from.models import *
# Create your views here.

def home(request):
    product=Products.objects.all()
    return render(request,'home.html',{'prod':product})

def productdetails(request,pk):
    proddet=Products.objects.get(id=pk)
    return render(request,'product.html',{'pr':proddet})          