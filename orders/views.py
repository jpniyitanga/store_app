from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from . models import Cart, CartItem, Product
from . serializers import CartItemSerializer, CartSerializer, AddCartItemSerializer


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
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        return CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_id']).select_related('product')

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_id']}


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    lookup_field = 'product_id'

    def get_object(self):
        product_id = self.kwargs.get(self.lookup_field)
        return get_object_or_404(CartItem, id=product_id)
