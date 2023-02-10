from django.urls import path
from.import views

urlpatterns=[
    path('',views.home,name='front'),
    path('product_view/<str:pk>/',views.productdetails,name='details')
]