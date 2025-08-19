from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView


class HomepageTemplateView(TemplateView):
    template_name = 'homepage.html'
