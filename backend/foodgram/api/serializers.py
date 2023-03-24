from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from users.models import User


class UserSignUpSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name',
                  'last_name', 'password')
