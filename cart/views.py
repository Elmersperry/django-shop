from django.shortcuts import render
from decimal import Decimal

from shop.models import Product
from .models import CartUser, CartItem
from shopproject.settings import CART_SESSION_ID

class Cart:
    """
    Класс корзины для анонимного пользователя (неавторизованного)
    """
    def __init__(self, request):
        # получаем текущую сессию
        self.session = request.session
        # получаем текущего пользователя
        self.user = request.user
        # получаем корзину из сессии или создаём новую
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    # сохранение изменений в сессии
    def save(self):
        self.session.modified = True

    # создание копии корзины
    def copy(self):
        return self.cart.copy()

    # метод добавления товара в корзину
    def add(self, product, quantity=1, override_quantity=False):
        # получаем id товара из ОБЪЕКТА товара
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        # если нужно перезаписать кол-во товаров
        if override_quantity:
            self.cart[product_id][quantity] = quantity
        else:
            self.cart[product_id][quantity] += quantity

        self.save()

    # метод удаления товара из корзины
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # метод подсчёта общего количества элементов в корзине
    def __len__(self):
        # считаем позиции в корзине
        # return len(self.cart)
        # считаем общее кол-во товаров в корзине
        return sum(item['quantity'] for item in self.cart.values())

    # подсчёт суммы товаров в корзине
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    # удаление всех товаров из корзины
    def clear(self):
        self.cart.clear()
        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
