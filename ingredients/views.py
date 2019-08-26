from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Ingredient, Recipe, IngrQuantity



def ingredients(request):
	context = {
		'ingredients': Ingredient.objects.all()
	}
	return render(request, 'ingredients/ingredients.html', context)



def recipes(request):
	context = {
		'recipes': Recipe.objects.all()
	}
	return render(request, 'ingredients/recipes.html', context)



def recipe(request, recipe_id):
	try:
		recipe = Recipe.objects.get(pk=recipe_id)
		recipeIngredients = IngrQuantity.objects.filter(recipe=recipe)

	except Recipe.DoesNotExist:
		raise Http404("Recipe does not exist")

	context = {
		'recipe': recipe, 
		'recipeIngredients': recipeIngredients, 
	}
	return render(request, 'ingredients/recipe.html', context)



def ingredient(request, ingredient_id):
	try:
		ingredient = Ingredient.objects.get(pk=ingredient_id)
		recipes = IngrQuantity.objects.filter(ingr=ingredient)

	except Ingredient.DoesNotExist:
		raise Http404("Ingredient does not exist")

	context = {
		'ingredient': ingredient, 
		'recipes': recipes, 
	}
	return render(request, 'ingredients/ingredient.html', context)



def add_recipe_page(request):
	context = {
		'ingredients': Ingredient.objects.all()
	}
	return render(request, 'ingredients/add_recipe.html', context)



def add_recipe_submit(request):
	try:
		recipe = Recipe.objects.get(pk=recipe_id)
		recipeIngredients = IngrQuantity.objects.filter(recipe=recipe)

	except Recipe.DoesNotExist:
		raise Http404("Recipe does not exist")

	context = {
		'recipe': recipe, 
		'recipeIngredients': recipeIngredients, 
	}
	return render(request, 'ingredients/recipe.html', context)