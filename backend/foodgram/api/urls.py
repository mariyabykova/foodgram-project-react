from django.urls import include, path
from rest_framework.routers import DefaultRouter

# from api.views import CustomUserViewSet


router = DefaultRouter()

# router.register('users', CustomUserViewSet, basename='users')

urlpatterns = [
    # path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
