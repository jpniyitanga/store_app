from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
