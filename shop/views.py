from django.shortcuts import render
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
    template_name = 'admin/add_category.html'
    success_url = reverse_lazy('staff:categories')

# Класс для просмотра категорий
class CategoryListView(ListView):
    model = Category
    template_name = 'admin/list_category.html'
    context_object_name = 'categories'