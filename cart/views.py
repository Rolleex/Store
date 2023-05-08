from django.shortcuts import render, get_object_or_404, redirect

from cart.cart import Cart
from .forms import CartAddForm
from shop.models import ProductItem


# Create your views here.
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
    return render(request, 'cart/cart_detail.html', context={'cart': cart})
