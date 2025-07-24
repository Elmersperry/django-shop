from django.db import models
from django.contrib.auth import get_user_model
from cart.models import CartUser
from shop.models import Product

User = get_user_model()

class Order(models.Model):
    number = models.CharField(primary_key=True, unique=True, max_length=256, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True)
    cart = models.OneToOneField(CartUser, on_delete=models.SET_NULL, editable=False, null=True)

    status = models.CharField(max_length=50, default='в обработке', editable=False)
    payment = models.CharField(max_length=50, default='картой')
    delivery = models.CharField(max_length=50, default='самовывоз из магазина')
    address = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return " ".join(
            ["Заказ № ", self.number, "пользователя", self.user.username, "от", self.created_at.strftime('%Y-%m-%d')])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def get_total_price(self):
        return self.product.price * self.quantity