from unicodedata import category

from django.shortcuts import render, get_object_or_404
from .forms import CategoryCreateForm, ProductCreateForm
from .models import Category, Product
from django.urls import reverse_lazy
from django.views.generic import (CreateView,
                                  DetailView,
                                  ListView,
                                  UpdateView,
                                  DeleteView)

             ###################### АДМИНКА ######################

# Класс для создания новой категории
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'admin_pages/add_category.html'
    success_url = reverse_lazy('staff:categories')

# Класс для просмотра категорий
class CategoryListView(ListView):
    paginate_by = 2
    model = Category
    template_name = 'admin_pages/list_category.html'
    context_object_name = 'categories'

# Класс для создания товара
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'admin_pages/add_product.html'
    success_url = reverse_lazy('staff:products')

# Класс для отображения товаров
class ProductListView(ListView):
    paginate_by = 2
    model = Product
    template_name = 'admin_pages/list_product.html'
    context_object_name = 'products'

# Класс для отображения информации о товаре
class ProductDetailView(DetailView):
    model = Product
    template_name = 'admin_pages/detail_product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


###################### КЛИЕНТ ######################

class ProductsByCategoryListView(ListView):
    paginate_by = 2
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context

    def get_queryset(self):
        # если не выбрана категория
        # возвращаем все товары
        if not self.kwargs.get('slug'):
            return Product.objects.all()
        # получаем название категории из URL
        # и возвращаем товары выбранной категории
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category=category)

class ProductDetailClientView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'
