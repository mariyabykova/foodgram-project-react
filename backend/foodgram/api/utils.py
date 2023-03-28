import base64

from django.shortcuts import get_object_or_404
from django.core.files.base import ContentFile
from rest_framework import serializers

from recipes.models import Ingredient, RecipeIngredient


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')  
            ext = format.split('/')[-1]  
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


def create_ingredients(ingredients, recipe):
    for ingredient in ingredients:
            current_ingredient = get_object_or_404(Ingredient, id=ingredient.get('id'))
            amount = ingredient.get('amount')
            RecipeIngredient.objects.create(
                    recipe=recipe,
                    ingredient=current_ingredient,
                    amount=amount
                )
