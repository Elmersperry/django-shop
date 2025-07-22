from django.shortcuts import render
import uuid
import json

from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, reverse, render

from .models import Order, OrderItem
from .forms import OrderForm
from cart.views import Cart, ProductCartUser
from cart.models import CartItem
from shop.models import Product

def new_order(request):
    cart = ProductCartUser(request)

    if request.method == 'GET':
        order_form = OrderForm()
        return render(request, template_name='orders/order_add.html', context={'form': order_form, 'cart': cart})

    if request.method == "POST":
        order_form = OrderForm(request.POST,
                               initial={"number": uuid.uuid4(), "user": request.user, "cart": cart.user_cart})
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.number = uuid.uuid4()
            order.user = request.user
            order.cart = cart.user_cart
            order.name = request.user.username
            order.save()

            for item in cart:
                OrderItem.objects.create(order=order_form.instance, product=item['product'], quantity=item['quantity'])
            cart.user_cart.delete()
        return render(request, template_name='orders/order_created.html', context={"order": order_form.instance})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders': orders}

    return render(request, template_name='orders/orders.html', context=context)

@login_required
def order_detail(request, number):
    order = get_object_or_404(Order, number=number)
    if request.user != order.user:
        raise PermissionDenied
    order_items = order.order_items.all()
    context = {'order': order, 'order_items': order_items}
    return render(request, template_name='orders/order_detail.html', context=context)