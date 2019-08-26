from django.contrib import admin

from .models import Ingredient_Unit, Ingredient, Recipe, IngrQuantity
admin.site.register(Ingredient_Unit)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(IngrQuantity)
