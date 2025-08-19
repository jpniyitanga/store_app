from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HomepageTemplateView(TemplateView):
    template_name = 'home.html'

    # class HomepageView(APIView):
    #     def get(self, request):
    #         data = {
    #             "message": "Welcome to Homepage",
    #             "message": "success"
    #         }
    #         return Response(data, status=status.HTTP_200_OK)
