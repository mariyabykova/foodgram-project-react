from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import TagViewSet


v1_router = DefaultRouter()

v1_router.register('tags', TagViewSet, basename='tags')

urlpatterns = [
    path('', include(v1_router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
