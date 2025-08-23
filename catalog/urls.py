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
    path('<slug:slug>/',
         ProductDetailView.as_view(), name='product-detail'),


    path('categories/', CategoryListView.as_view(), name='category-list'),

    path('categories/<slug:slug>/',
         CategoryProductListView.as_view(), name='category-product-list'),

    path('brands/', BrandListView.as_view(), name='brand-list'),

    path('brands/<slug:slug>/',
         BrandProductListView.as_view(), name='brand-product-list'),

    path('promotions/<int:promotion_id>/',
         ProductByPromotionListView.as_view(), name='products-by-promotion'),

    path('tags/<slug:tag_slug>/',
         ProductByTagListView.as_view(), name='products-by-tag'),

    path('', ProductListView.as_view(), name='product-list'),
]
