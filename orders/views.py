from django.shortcuts import render
from .forms import OrderModelForms
from cart.cart import Cart
from .models import OrderItem


# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderModelForms(request.POST)
        if form.is_valid():
            order = form.save()
            for items in cart:
                OrderItem.objects.create(order=order,
                                         productitem=items['product'],
                                         price=items['price'],
                                         quantity=items['quantity']
                                         )
            cart.clear()
            return render(request, 'orders/order_created.html', context={'order': order})
    else:
        form = OrderModelForms
    return render(request, 'orders/order_create.html', context={'cart': cart, 'form': form})
