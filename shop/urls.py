from django.urls import path
from .views import ProductsByCategoryListView, ProductDetailClientView

app_name = 'shop'
urlpatterns = [
    path('products/<slug:slug>/info/', ProductDetailClientView.as_view(), name='product_detail'),
    path('products/<slug:slug>/', ProductsByCategoryListView.as_view(), name='index_category'),
    path('', ProductsByCategoryListView.as_view(), name='index'),
]