from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers

from accounts.models import Account


class CustomUserCreateSerializer(BaseUserCreateSerializer):
    phone_number = serializers.CharField(required=False)
    birth_date = serializers.DateField(required=False)
    street = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    province = serializers.CharField(required=False)
    postal_code = serializers.CharField(required=False)
    country = serializers.CharField(required=False)

    class Meta(BaseUserCreateSerializer.Meta):
        model = Account
        fields = ['first_name', 'last_name',
                  'username', 'email']


class CustomUserRetrieveSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=False)
    birth_date = serializers.DateField(required=False)
    street = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    province = serializers.CharField(required=False)
    postal_code = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    date_joined = serializers.DateTimeField()

    class Meta:
        model = Account
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'phone_number',
                  'birth_date', 'street', 'city', 'province', 'postal_code', 'country', 'date_joined']
        read_only_fields = ('id', 'date_joined')
