from email.policy import default
from uuid import uuid4
from rest_framework import serializers
from . models import Cart, CartItem
from catalog.models import Product
from catalog.serializers import ProductSerializer


class CartItemProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price']


class CartItemSerializer(serializers.ModelSerializer):
    product = CartItemProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

    # total_price = serializers.SerializerMethodField(
    #     method_name='calculate_total_price')

    # def calculate_total_price(self, cart_item: CartItem):
    #     return cart_item.product__price * cart_item.quantity


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'items']
