from django.db import models
from django.urls import reverse



class Ingredient_Unit(models.Model):
	unit = models.CharField(max_length=16, unique=True)
	
	def __str__(self):
		return self.unit



class Ingredient(models.Model):
	name = models.CharField(max_length=64)#, related_name="ingredients")
	unit = models.ForeignKey(Ingredient_Unit, on_delete=models.CASCADE)
	wiki = models.URLField(max_length=250, default='')
	
	def __str__(self):
		return f"{self.name}, {self.unit}"

	def get_absolute_url(self):
		return reverse('ingredient-page', kwargs={'ingredient_id': self.pk})



class Recipe(models.Model):
	name = models.CharField(max_length=64)
	recipe_yield = models.IntegerField()
	recipeIngredients = models.ManyToManyField(Ingredient, through='IngrQuantity', related_name='rec_ingredients')
	instructions = models.TextField()

	def __str__(self):
		return f"{self.name}"



class IngrQuantity(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	ingr = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	quantity = models.FloatField()
	
	def __str__(self):
		return f"{self.recipe}, {self.ingr}, {self.quantity}"
