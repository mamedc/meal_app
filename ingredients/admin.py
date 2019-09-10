from django.contrib import admin

from .models import (
	IngredientUnit, 
	Ingredient, 
	BaseRecipe, 
	BaseRec_Ingredient_Amount,	
	Recipe,
	Rec_Ingredient_Amount,
	Rec_bRec_Amount,
)

admin.site.register(IngredientUnit)
admin.site.register(Ingredient)
admin.site.register(BaseRecipe)
admin.site.register(BaseRec_Ingredient_Amount)
admin.site.register(Recipe)
admin.site.register(Rec_Ingredient_Amount)
admin.site.register(Rec_bRec_Amount)
