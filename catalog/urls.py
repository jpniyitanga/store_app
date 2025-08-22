from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    CategoryListView,
    CategoryProductListView,
    BrandListView,
    BrandProductListView,
    ProductByPromotionListView,
    ProductByTagListView
)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<slug:slug>/',
         ProductDetailView.as_view(), name='product-detail'),


    path('products/categories/', CategoryListView.as_view(), name='category-list'),

    path('products/categories/<slug:slug>/',
         CategoryProductListView.as_view(), name='category-product-list'),

    path('products/brands/', BrandListView.as_view(), name='brand-list'),

    path('products/brands/<slug:slug>/',
         BrandProductListView.as_view(), name='brand-product-list'),

    path('products/promotions/<int:promotion_id>/',
         ProductByPromotionListView.as_view(), name='products-by-promotion'),

    path('products/tags/<slug:tag_slug>/',
         ProductByTagListView.as_view(), name='products-by-tag'),

]
