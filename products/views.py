from django.shortcuts import render
from rest_framework import generics
from . models import Product
from . serializers import ProductSerializer

# Create your views here.


class ProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
