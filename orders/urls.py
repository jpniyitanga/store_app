from django.urls import path
from . views import CartCreateView

urlpatterns = [
    path('carts/', CartCreateView.as_view(), name='cart-create')
]
