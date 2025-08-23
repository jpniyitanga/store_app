from django.urls import path, include


urlpatterns = [
    # path('products/', include('products.urls')),
    path('store/products/', include('catalog.urls')),
    path('store/orders/', include('orders.urls')),
]
