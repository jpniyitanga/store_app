from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import CustomUserViewSet

router = DefaultRouter()
# We use 'users' here instead of 'auth/users' because the 'auth/' prefix will be added in the next step.
router.register(r'users', CustomUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
