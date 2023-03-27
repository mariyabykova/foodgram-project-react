from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (IngredientViewSet, TagViewSet, UserSubscribeView,
                       UserSubscriptionsViewSet)


v1_router = DefaultRouter()

v1_router.register(r'users/subscriptions', UserSubscriptionsViewSet, basename='subscriptions')
v1_router.register('tags', TagViewSet, basename='tags')
v1_router.register('ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('users/<int:user_id>/subscribe/', UserSubscribeView.as_view()),
    path('', include(v1_router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
