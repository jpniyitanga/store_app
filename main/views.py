from django.views.generic import TemplateView
from django.shortcuts import render
from django.db.models import F, ExpressionWrapper, Value, DecimalField
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from catalog.models import Product, Category


# class HomepageTemplateView(TemplateView):
#     template_name = 'home.html'


def get_products(request):

    queryset = Product.objects.select_related('category').all()

    # queryset = Product.objects.values('name', 'price')
    # queryset = Product.objects.filter(
    #     price__lt=10.00, category__name__icontains='food').order_by('name')

    # return request, template, context represented by a dict
    return render(request, 'home.html', {'name': 'Jean', 'products': list(queryset)})
