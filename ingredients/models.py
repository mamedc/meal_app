from django.db import models


class Ingredient_Unit(models.Model):
	unit = models.CharField(max_length=16)

	def __str__(self):
		return self.unit


class Ingredient(models.Model):
	name = models.CharField(max_length=64)#, related_name="ingredients")
	unit = models.ForeignKey(Ingredient_Unit, on_delete=models.CASCADE)
	wiki = models.URLField(max_length=250, default='')
	
	def __str__(self):
		return f"{self.name}, {self.unit}, {self.wiki}"


class Recipe(models.Model):
	name = models.CharField(max_length=64)
	recipe_yield = models.IntegerField()
	recipeIngredients = models.ManyToManyField(Ingredient, through='IngrQuantity', related_name='rec_ingredients')

	def __str__(self):
		return f"{self.name}, {self.recipe_yield}"


class IngrQuantity(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	ingr = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	quantity = models.FloatField()
	
	def __str__(self):
		return f"{self.recipe}, {self.ingr}, {self.quantity}"
