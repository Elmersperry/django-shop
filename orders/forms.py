from django import forms
from .constants import PAYMENT_CHOISES, DELIVERY_CHOISES
from .models import Order

class QuickOrderForm(forms.Form):
    name = forms.CharField(max_length=50, label='Имя')
    last_name = forms.CharField(max_length=50, label='Фамилия')
    email = forms.EmailField(label="Эл.почта")
    phone = forms.CharField(max_length=20, label="Телефон")
    payment = forms.ChoiceField(choices=PAYMENT_CHOISES, label="Способ оплаты")
    delivery = forms.ChoiceField(choices=DELIVERY_CHOISES, label="Способ получения")


class OrderForm(forms.ModelForm):
    payment = forms.ChoiceField(choices=PAYMENT_CHOISES, label="Способ оплаты")
    delivery = forms.ChoiceField(choices=DELIVERY_CHOISES, label="Способ получения")

    class Meta:
        model = Order
        exclude = ('name', 'last_name', 'email', 'phone', 'address')