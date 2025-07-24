from django import forms
from .models import Category, Product

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('slug', 'created_at', 'updated')