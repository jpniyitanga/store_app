from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from . models import Cart, CartItem
from . serializers import CartItemSerializer, CartSerializer


class CartCreateView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetailView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    lookup_field = 'id'

    def get_object(self):
        id = self.kwargs.get(self.lookup_field)
        return get_object_or_404(Cart, id=id)
