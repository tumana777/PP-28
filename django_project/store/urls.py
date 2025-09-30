from django.urls import path
from store.views import (IndexView, products_json,
    ProductListView, ProductDetailView, ProductCreateView,
    ProductUpdateView, ProductDeleteView
)

from django.views.generic import TemplateView

app_name = 'store'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('products.json/', products_json, name='products_json'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:product_pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('update_product/<int:product_pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:product_pk>/', ProductDeleteView.as_view(), name='delete_product'),
]
