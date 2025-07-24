from django.urls import path
from .views import new_order

app_name = 'orders'
urlpatterns = [
    path('new/', new_order, name='new_order'),
]