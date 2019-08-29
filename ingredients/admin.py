from django.contrib import admin

from .models import (
	IngredientUnit, 
	Ingredient, 
	BaseRecipe, 
	BaseRec_Ingredient_Amount,	
)

admin.site.register(IngredientUnit)
admin.site.register(Ingredient)
admin.site.register(BaseRecipe)
admin.site.register(BaseRec_Ingredient_Amount)
