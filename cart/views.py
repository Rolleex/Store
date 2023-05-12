import json

from django.core.serializers import serialize
from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from cart.cart import Cart
from shop.serializers import ProductItemSerializer
from .forms import CartAddForm
from shop.models import ProductItem
from rest_framework import generics, viewsets
from django.contrib.sessions.backends.db import SessionStore


# Create your views here.
##################
# DRF

class CartAPIView(viewsets.ViewSet):
    # permission_classes = []

    def list(self, request):
        session = SessionStore(session_key=request.session.session_key)
        data = session._session['cart']
        return Response(data)


###################


def cart_add(request, pk):
    product = get_object_or_404(ProductItem, pk=pk)
    cart = Cart(request)
    form = CartAddForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('home')


def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(ProductItem, pk=pk)
    cart.remove(product)
    return redirect(request.META.get('HTTP_REFERER'))


def cart_detail(request):
    cart = Cart(request)
    print(cart)
    return render(request, 'cart/cart_detail.html', context={'cart': cart})
