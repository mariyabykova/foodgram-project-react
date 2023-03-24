from djoser.views import UserViewSet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.serializers import UserGetSerializer
from users.models import User


# class CustomUserViewSet(UserViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserGetSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, )
