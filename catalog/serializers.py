from rest_framework import serializers
from . models import Product, Category, Brand


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description',
                  'price', 'stock', 'category', 'is_available']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class BrandProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']
