from django.urls import path, include


urlpatterns = [
    # path('products/', include('products.urls')),
    path('store/', include('catalog.urls')),
]
