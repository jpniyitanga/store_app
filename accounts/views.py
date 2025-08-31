from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied


class CustomUserViewSet(UserViewSet):
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        raise PermissionDenied("Deleting your account is not allowed.")
