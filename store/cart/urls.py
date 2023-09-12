from django.urls import path
from .views import *

urlpatterns = [

    path('detail/', cart_detail, name='cart_detail'),
    path('add/<int:pk>', cart_add, name='cart_add'),
    path('detail/<int:pk>', cart_remove, name='cart_remove'),
    path('api/v1/cart', CartAPIView.as_view({'get': 'list'}))

]
