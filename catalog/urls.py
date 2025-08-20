from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    CategoryListView,
    CategoryProductListView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<slug:slug>/',
         ProductDetailView.as_view(), name='product-detail'),
    path('', CategoryListView.as_view(), name='category-list'),
    path('<slug:slug>/products/',
         CategoryProductListView.as_view(), name='category-product-list'),
]
