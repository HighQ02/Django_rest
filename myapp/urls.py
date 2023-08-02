from django.urls import path
from .views import *

urlpatterns = [
    path('all_products', ProductApiView.as_view(), name='all_products_url'),
    path('product_detail', ProductDetailApiView.as_view(), name='product_detail_url'),
]
