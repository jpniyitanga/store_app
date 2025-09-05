import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    # Filter by related slugs
    category = django_filters.CharFilter(
        field_name="category__slug", lookup_expr="exact")
    brand = django_filters.CharFilter(
        field_name="brand__slug", lookup_expr="exact")
    tag = django_filters.CharFilter(
        field_name="tags__slug", lookup_expr="exact")
    promotion = django_filters.CharFilter(
        field_name="promotions__slug", lookup_expr="exact")

    # Price range filters
    min_price = django_filters.NumberFilter(
        field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(
        field_name="price", lookup_expr="lte")

    # Optional: filter by availability dates (assuming your Product has a `date_added` or `available_from` field)
    date_added_after = django_filters.DateFilter(
        field_name="date_added", lookup_expr="gte")
    date_added_before = django_filters.DateFilter(
        field_name="date_added", lookup_expr="lte")

    class Meta:
        model = Product
        fields = [
            "category", "brand", "tag", "promotion",
            "min_price", "max_price", "date_added_after", "date_added_before"
        ]
