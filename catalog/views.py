from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from .models import Product, Category, Brand, Promotion
from .filters import ProductFilter
from .serializers import ProductSerializer, CategorySerializer, BrandProductListSerializer, BrandSerializer, PromotionSerializer


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - SAFE_METHODS (GET, HEAD, OPTIONS) → everyone can access
    - POST, PUT, PATCH, DELETE → only admins
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]

    # Add search & ordering
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'date_added']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=True, methods=['get'])
    def products(self, request, slug=None):
        category = self.get_object()
        queryset = Product.objects.filter(
            category=category, is_available=True)

        # You can apply pagination and filtering here if needed
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ProductSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=True, methods=['get'])
    def products(self, request, slug=None):
        brand = self.get_object()
        queryset = Product.objects.filter(brand=brand, is_available=True)

        # You can apply pagination and filtering here if needed
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = BrandProductListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = BrandProductListSerializer(queryset, many=True)
        return Response(serializer.data)
