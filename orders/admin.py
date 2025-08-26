from decimal import Decimal
from django.contrib import admin
from django.utils.html import format_html
from accounts.models import Account
from .models import Order, OrderItem, Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
    fields = ('product', 'quantity')


@admin.register(Cart)
class CartItemAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ('id', 'created_at')
    readonly_fields = ('id',)
    inlines = [CartItemInline]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('id', 'placed_at', 'payment_status')


admin.site.register(OrderItem)
