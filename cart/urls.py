from django.urls import path
from .views import cart_detail, remove_product, remove_cart

app_name = 'cart'
urlpatterns = [
    path('detail/', cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', remove_product, name='remove_product'),
    path('clear/', remove_cart, name='remove_cart'),
]