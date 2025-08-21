from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    CategoryListView,
    CategoryProductListView,
    BrandListView,
    BrandProductListView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<slug:slug>/',
         ProductDetailView.as_view(), name='product-detail'),

    path('categories/', CategoryListView.as_view(), name='category-list'),

    path('categories/<slug:slug>/products/',
         CategoryProductListView.as_view(), name='category-product-list'),

    path('brands/', BrandListView.as_view(), name='brand-list'),

    path('brands/<slug:slug>/products/',
         BrandProductListView.as_view(), name='brand-product-list'),
]
