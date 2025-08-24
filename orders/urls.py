from django.urls import path
from . views import CartCreateView, CartDetailView, CartItemListView, CartItemDetailView

urlpatterns = [
    path('carts/', CartCreateView.as_view(), name='cart-create'),
    path('carts/<str:cart_id>/', CartDetailView.as_view(), name='cart-detail'),
    path('carts/<str:cart_id>/items/',
         CartItemListView.as_view(), name='cart-items'),
    path('carts/<str:cart_id>/items/<int:product_id>/',
         CartItemDetailView.as_view(), name='cart-item-detail'),
]
