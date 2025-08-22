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
    path('', ProductListView.as_view(), name='product-list'),

    path('categories/', CategoryListView.as_view(), name='category-list'),

    path('categories/<slug:slug>/products/',
         CategoryProductListView.as_view(), name='category-product-list'),

    path('brands/', BrandListView.as_view(), name='brand-list'),

    path('brands/<slug:slug>/products/',
         BrandProductListView.as_view(), name='brand-product-list'),

    path('products/promotion/<int:promotion_id>',
         ProductByPromotionListView.as_view(), name='products-by-promotion'),

    path('products/tag/<slug:tag_slug>/',
         ProductByTagListView.as_view(), name='products-by-tag'),
    path('<slug:slug>/',
         ProductDetailView.as_view(), name='product-detail'),

]
