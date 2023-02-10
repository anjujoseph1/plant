from django.urls import path
from.import views

urlpatterns=[
    path('cartt/',views.cartproducts,name='cartdet'),
    path('add/<int:product_id>/',views.addcart,name='addcart'),
]