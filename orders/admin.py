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
    readonly_fields = ('id',)
    inlines = [CartItemInline]


admin.site.register(Order)
admin.site.register(OrderItem)
