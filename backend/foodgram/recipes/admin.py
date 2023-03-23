from django.contrib import admin

from recipes.models import (Favorite,  Ingredient, Recipe,
                             RecipeIngredient, ShoppingCart,  Tag)


admin.site.register(Favorite)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(ShoppingCart)
admin.site.register(Tag)
