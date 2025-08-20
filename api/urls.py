from django.urls import path, include
from products.views import ProductsView, ProductDetailView


urlpatterns = [
    # path('products/', include('products.urls')),
    path('products/', include('catalog.urls')),
    path('category/', include('catalog.urls')),
]
