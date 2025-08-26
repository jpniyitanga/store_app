from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
from .models import Product, Category, Brand, Tag, Promotion


class ProductInline(admin.TabularInline):
    model = Product
    prepopulated_fields = {'slug': ('name',)}
    extra = 1
    fields = ('name', 'slug', 'price', 'stock',
              'is_available', 'image_url', 'brand')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_display = ('name', 'slug', 'products_count')
    inlines = [ProductInline]

    # Define computed field and make it sortable
    @admin.display(ordering='products_count')
    def products_count(self, category):
        # return category.products_count
        # ('admin:app_targetModel_page)
        url = (reverse('admin:catalog_product_changelist')
               # Apply filter to show products in the selected category
               + '?'
               + urlencode({'category__id': str(category.id)}))
        return format_html('<a href={}>{}</a>', url, category.products_count)

    # Change queryset default behavior to count products instead of categories
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product'))


# Custom Filter
class InventoryFilter(admin.SimpleListFilter):
    title = 'Inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<60', 'Low')
        ]

    def queryset(self, request, queryset):
        if self.value() == '<60':
            return queryset.filter(stock__lt=60)


class PromotionFilter(admin.SimpleListFilter):
    title = 'Promotions'
    parameter_name = 'promotions'

    def lookups(self, request, model_admin):
        promotions = Promotion.objects.all()
        return [(promo.slug, promo.title) for promo in promotions]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(promotions__slug=self.value())
        return queryset


class TagFilter(admin.SimpleListFilter):
    title = 'Tags'
    parameter_name = 'tags'

    def lookups(self, request, model_admin):
        tags = Tag.objects.all()
        return [(tag.slug, tag.name) for tag in tags]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(tags__name=self.value())
        return queryset


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'price', 'inventory_status', 'category']
    list_editable = ['price']
    list_per_page = 20
    list_select_related = ['category']
    # Create  search field with case insensitive
    search_fields = ['name__icontains']
    # Create a filter for categories
    list_filter = ['category', InventoryFilter, PromotionFilter, TagFilter]
    autocomplete_fields = ['category']

    @admin.display(ordering='stock')  # Sorting by new computed column
    def inventory_status(self, product):
        if product. stock < 60:
            return 'Low'
        return 'OK'


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'discount_percentage', 'start_date', 'end_date')
