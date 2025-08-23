from django.urls import path
from . views import CartCreateView, CartDetailView

urlpatterns = [
    path('carts/', CartCreateView.as_view(), name='cart-create'),
    path('carts/<str:id>/', CartDetailView.as_view(), name='cart-detail'),
]
