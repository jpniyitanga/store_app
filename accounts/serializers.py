from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers

from accounts.models import Account


class CustomUserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = Account
        fields = ['phone_number', 'birth_date', 'street',
                  'city', 'province', 'postal_code', 'country']
