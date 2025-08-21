from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Product, Category, Brand
from .serializers import ProductSerializer, CategorySerializer, BrandProductListSerializer, BrandSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_available=True)
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_available=True)
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class ProductByPromotionListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        promotion_id = self.kwargs['promotion_id']
        return Product.objects.filter(promotion__id=promotion_id)


class ProductByTagListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        return Product.objects.filter(tags__slug=tag_slug)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_slug = self.kwargs['slug']
        return Product.objects.filter(category__slug=category_slug, is_available=True)


class BrandListView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandProductListView(generics.ListAPIView):
    serializer_class = BrandProductListSerializer

    def get_queryset(self):
        brand_slug = self.kwargs['slug']
        return Product.objects.filter(brand__slug=brand_slug, is_available=True)
