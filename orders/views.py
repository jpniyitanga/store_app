from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from . models import Cart, CartItem, Product
from . serializers import CartItemSerializer, CartSerializer


class CartCreateView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    lookup_field = 'cart_id'

    def get_object(self):
        cart_id = self.kwargs.get(self.lookup_field)
        return get_object_or_404(Cart.objects.prefetch_related('items__product').filter(id=cart_id))


class CartItemListView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    lookup_field = 'product_id'

    def get_object(self):
        product_id = self.kwargs.get(self.lookup_field)
        return get_object_or_404(CartItem, id=product_id)
