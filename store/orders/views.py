from django.shortcuts import render
from .forms import OrderModelForms
from cart.cart import Cart
from .models import OrderItem, OrderModel


# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        if request.user.is_authenticated:
            user_profile = request.user.profile
            form = OrderModelForms(request.POST, initial={
                'first_name': user_profile.first_name,
                'last_name': user_profile.last_name,
                'email': request.user.email,
                'address': user_profile.address,
                'city': user_profile.city,
            })
        else:
            form = OrderModelForms(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    productitem=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            return render(request, 'orders/order_created.html', context={'order': order})
    else:
        if request.user.is_authenticated:
            user_profile = request.user.profile
            form = OrderModelForms(initial={
                'first_name': user_profile.first_name,
                'last_name': user_profile.last_name,
                'email': request.user.email,
                'address': user_profile.address,
                'city': user_profile.city,
            })
        else:
            form = OrderModelForms()
    return render(request, 'orders/order_create.html', context={'cart': cart, 'form': form})