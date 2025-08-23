from django.shortcuts import render
from rest_framework import generics
from . models import Cart, CartItem
from . serializers import CartItemSerializer, CartSerializer


class CartCreateView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
