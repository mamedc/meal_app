from django.db import models
from django.urls import reverse


class IngredientUnit(models.Model):
	unitName = models.CharField(max_length=16, unique=True)
	unitSymbol = models.CharField(max_length=8, unique=True)
	def __str__(self):
		return f"{self.unitName} ({self.unitSymbol})"


class Ingredient(models.Model):
	name = models.CharField(max_length=64, unique=True)
	unit = models.ManyToManyField('IngredientUnit', related_name="ingredients")
	wiki = models.URLField(max_length=250, default=None)
	def __str__(self): 
		return f"{self.name}"
	

class BaseRecipe(models.Model):
	name = models.CharField(max_length=64, unique=True)
	brec_yield_unit = models.ForeignKey(IngredientUnit, on_delete=models.PROTECT, related_name="baseRecipes")
	brec_yield_value = models.FloatField()
	brec_ingredients = models.ManyToManyField(Ingredient, through='BaseRec_Ingredient_Amount', related_name='baseRecipes')
	procedure = models.TextField()
	def __str__(self):
		return f"{self.name.capitalize()}"


class BaseRec_Ingredient_Amount(models.Model):
	baseRecipe = models.ForeignKey(BaseRecipe, on_delete=models.PROTECT, related_name='brec_ingredient_amount')
	ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT, related_name='brec_ingredient_amount')
	ingredientUnit = models.ForeignKey(IngredientUnit, on_delete=models.PROTECT)
	amount = models.FloatField()
	def __str__(self):
		return f"{self.baseRecipe.name}, {self.ingredient.name}, {self.amount}"


class Recipe(models.Model):
	name = models.CharField(max_length=64, unique=True)
	recipe_yield = models.IntegerField()
	recipeIngredients = models.ManyToManyField(Ingredient, through='Rec_Ingredient_Amount', related_name='rec_ingredients')
	recipeBaseRecipes = models.ManyToManyField(BaseRecipe, through='Rec_bRec_Amount', related_name='recBaseRec')
	procedure = models.TextField()
	def __str__(self):
		return f"{self.name.capitalize()}"


class Rec_Ingredient_Amount(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT, related_name='rec_ingredient_amount')
	ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT, related_name='rec_ingredient_amount')
	ingredientUnit = models.ForeignKey(IngredientUnit, on_delete=models.PROTECT)
	amount = models.FloatField()
	def __str__(self):
		return f"{self.recipe.name}, {self.ingredient.name}, {self.amount}"


class Rec_bRec_Amount(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT, related_name='brec_amount')
	brec = models.ForeignKey(BaseRecipe, on_delete=models.PROTECT, related_name='brec_amount')
	amount = models.FloatField()
	def __str__(self):
		return f"{self.recipe.name}, {self.brec.name}, {self.amount}"


