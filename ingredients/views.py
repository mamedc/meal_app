from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, resolve
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView
from django.contrib import messages

from .models import (
    IngredientUnit, 
    Ingredient, 
    BaseRecipe, 
    BaseRec_Ingredient_Amount, 
    Recipe, Rec_Ingredient_Amount, 
    Rec_bRec_Amount, 
)

from .forms import IngredientForm, BaseRecipeForm, RecipeForm


def addIngredient(request):
    # POST, generate form with data from the request
	if request.method == "POST":
		form = IngredientForm(request.POST)
        
		if form.is_valid():
			ingrName = form.cleaned_data['name'].lower()
			wikiUrl = form.cleaned_data['wiki']
			unitObj = form.cleaned_data['unit']

			# If ingrName already exists, return to POST form with flash msg
			if ingrName in Ingredient.objects.values_list('name', flat=True):
				messages.warning(request, 'Ingredient *{}* already exists!'.format(ingrName))
				return render(request, 'ingredients/addIngredient.html', {'form': form})

			# As it is a ManyToMany, 1st we save Ingredient than add the relationships
			ingrObj = Ingredient(name=ingrName, wiki=wikiUrl)
			ingrObj.save()
			for obj in unitObj:
				ingrObj.unit.add(obj)

        	# Success msg
			messages.success(request, 'Ingredient *{}* was created!'.format(ingrName))

			# Redirect to a new url
			return HttpResponseRedirect('/add_ingredient/')
    
	# GET, generate blank form
	else:
		form = IngredientForm()

	return render(request, 'ingredients/addIngredient.html', {'form': form})



def addBaseRecipe(request):
    # POST, generate form with data from the request
	if request.method == "POST":
		form = BaseRecipeForm(request.POST)
		form.is_valid() # Generates 'cleaned_data' and 'errors' dict
		
		# If brecName already exists, return to POST form with flash msg
		if form.cleaned_data['name'] in BaseRecipe.objects.values_list('name', flat=True):
			messages.warning(request, 'Base recipe *{}* already exists!'.format(form.cleaned_data['name']))
			return render(request, 'ingredients/addBaseRecipe.html', {'form': form})

		# As it is a ManyToMany, 1st we save Base Recipe, than add the relationships
		brecObj = BaseRecipe(
			name = form.cleaned_data['name'], 
			brec_yield_unit = form.cleaned_data['brec_yield_unit'], 
			brec_yield_value = form.cleaned_data['brec_yield_value'], 
			procedure = form.cleaned_data['procedure'])
		brecObj.save()

		n_ingrs = min([int(x) for x in set([x.split('_')[-1] for x in form.errors.keys()])])-1
		for i in range(1, n_ingrs+1):
			ingrAmountObj = BaseRec_Ingredient_Amount(
				baseRecipe = brecObj, 
				ingredient = form.cleaned_data['brec_ingr_name_' + str(i)],
				ingredientUnit = form.cleaned_data['brec_ingr_unit_' + str(i)],
				amount = form.cleaned_data['brec_ingr_val_' + str(i)])
			ingrAmountObj.save()
			#brecObj.brec_ingredients.add(ingrAmountObj)
		
		# Success msg
		messages.success(request, 'Base recipe *{}* was created!'.format(form.cleaned_data['name']))

		# Redirect to a new url
		return HttpResponseRedirect('/add_baserecipe/')

	# GET, generate blank form
	else:
		form = BaseRecipeForm()
	
	return render(request, 'ingredients/addBaseRecipe.html', {'form': form})



def addRecipe(request):
    # POST, generate form with data from the request
	if request.method == "POST":
		form = RecipeForm(request.POST)
		form.is_valid() # Generates 'cleaned_data' and 'errors' dict
		
		#assert False, 'XXXXXXXXX'

		# If recName already exists, return to POST form with flash msg
		if form.cleaned_data['name'] in Recipe.objects.values_list('name', flat=True):
			messages.warning(request, 'Recipe *{}* already exists!'.format(form.cleaned_data['name']))
			return render(request, 'ingredients/addRecipe.html', {'form': form})

		# As it is a ManyToMany, 1st we save Base Recipe, than add the relationships
		recObj = Recipe(
			name = form.cleaned_data['name'], 
			recipe_yield = form.cleaned_data['recipe_yield'], 
			procedure = form.cleaned_data['procedure'])
		recObj.save()


		n_ingrs = min([int(x) for x in set([x.split('_')[-1] for x in form.errors.keys() if x[:8] == 'rec_ingr'])])-1
		for i in range(1, n_ingrs+1):
			ingrAmountObj = Rec_Ingredient_Amount(
				recipe = recObj, 
				ingredient = form.cleaned_data['rec_ingr_name_' + str(i)],
				ingredientUnit = form.cleaned_data['rec_ingr_unit_' + str(i)],
				amount = form.cleaned_data['rec_ingr_val_' + str(i)])
			ingrAmountObj.save()
			

		n_brecs = min([int(x) for x in set([x.split('_')[-1] for x in form.errors.keys() if x[:8] == 'rec_brec'])])-1
		for i in range(1, n_brecs+1):
			bRecAmountObj = Rec_bRec_Amount(
				recipe = recObj, 
				brec = form.cleaned_data['rec_brec_name_' + str(i)],
				amount = form.cleaned_data['rec_brec_val_' + str(i)])
			bRecAmountObj.save()
			

		# Success msg
		messages.success(request, 'Recipe *{}* was created!'.format(form.cleaned_data['name']))

		# Redirect to a new url
		return HttpResponseRedirect('/add_recipe/')

	# GET, generate blank form
	else:
		form = RecipeForm()
	
	return render(request, 'ingredients/addRecipe.html', {'form': form})




# def ingredients(request):
# 	context = {'ingredients': Ingredient.objects.all()}
# 	return render(request, 'ingredients/ingredients.html', context)



# def recipes(request):
# 	context = {
# 		'current_url': resolve(request.path_info).url_name, 
# 		'recipes': Recipe.objects.all()}
# 	return render(request, 'ingredients/recipes.html', context)


# # Class View for all recipes
# class RecipeListView(ListView):
# 	model = Recipe
# 	template_name = 'ingredients/recipes.html'
# 	context_object_name = 'recipes' # as in the context of the function Recipes above
# 	ordering = ['name'] # this will sort the recipes by name


# # Detailed View for specific Recipe
# class RecipeDetailView(DetailView):
# 	model = Recipe
# 	# automaticaly, the view searches for a template with name as
# 	# <app>/<model>_<viewtype>.html
# 	# We have to create it


# # Create View
# class IngredientCreateView(CreateView):
# 	model = Ingredient
# 	fields = ['name', 'unit', 'wiki']
# 	def get_success_url(self):
# 		return reverse('ingredients-page')



# def recipe(request, recipe_id):
# 	try:
# 		recipe = Recipe.objects.get(pk=recipe_id)
# 		recipeIngredients = IngrQuantity.objects.filter(recipe=recipe)

# 	except Recipe.DoesNotExist:
# 		raise Http404("Recipe does not exist")

# 	context = {
# 		'recipe': recipe, 
# 		'recipeIngredients': recipeIngredients, 
# 	}
# 	return render(request, 'ingredients/recipe.html', context)



# def ingredient(request, ingredient_id):
# 	try:
# 		ingredient = Ingredient.objects.get(pk=ingredient_id)
# 		recipes = IngrQuantity.objects.filter(ingr=ingredient)

# 	except Ingredient.DoesNotExist:
# 		raise Http404("Ingredient does not exist")

# 	context = {
# 		'ingredient': ingredient, 
# 		'recipes': recipes, 
# 	}
# 	return render(request, 'ingredients/ingredient.html', context)



# def add_recipe_page(request):
    
#     if request.method == 'POST':
#         form = RecipeForm(request.POST, extra=request.POST.get('extra_field_count'))
#         if form.is_valid():
#             print("valid!")
    
#     else:
#         form = RecipeForm()
    
#     return render(request, 'ingredients/add_recipe.html', {'form': form})



# def add_recipe_submit(request):
# 	try:
# 		recipe = Recipe.objects.get(pk=recipe_id)
# 		recipeIngredients = IngrQuantity.objects.filter(recipe=recipe)

# 	except Recipe.DoesNotExist:
# 		raise Http404("Recipe does not exist")

# 	context = {
# 		'recipe': recipe, 
# 		'recipeIngredients': recipeIngredients, 
# 	}
# 	return render(request, 'ingredients/recipe.html', context)



# class RecipeCreateView(TemplateView):
#     template_name = "ingredients/recipe_create.html"
    
#     def get(self, request):
#     	form_class = RecipeForm
#     	return render(request, self.template_name, {'form': form_class})



# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.db import IntegrityError, transaction
# from django.forms.formsets import formset_factory
# from .forms import LinkForm, BaseLinkFormSet, ProfileForm
# #from .models import UserLink

# def test_profile_settings(request):
#     """
#     Allows a user to update their own profile.
#     """
#     user = request.user

#     # Create the formset, specifying the form and formset we want to use.
#     LinkFormSet = formset_factory(LinkForm, formset=BaseLinkFormSet)

#     # Get our existing link data for this user.  This is used as initial data.
#     user_links = UserLink.objects.filter(user=user).order_by('anchor')
#     link_data = [{'anchor': l.anchor, 'url': l.url}
#                     for l in user_links]

#     if request.method == 'POST':
#         profile_form = ProfileForm(request.POST, user=user)
#         link_formset = LinkFormSet(request.POST)

#         if profile_form.is_valid() and link_formset.is_valid():
#             # Save user info
#             user.first_name = profile_form.cleaned_data.get('first_name')
#             user.last_name = profile_form.cleaned_data.get('last_name')
#             user.save()

#             # Now save the data for each form in the formset
#             new_links = []

#             for link_form in link_formset:
#                 anchor = link_form.cleaned_data.get('anchor')
#                 url = link_form.cleaned_data.get('url')

#                 if anchor and url:
#                     new_links.append(UserLink(user=user, anchor=anchor, url=url))

#             try:
#                 with transaction.atomic():
#                     #Replace the old with the new
#                     UserLink.objects.filter(user=user).delete()
#                     UserLink.objects.bulk_create(new_links)

#                     # And notify our users that it worked
#                     messages.success(request, 'You have updated your profile.')

#             except IntegrityError: #If the transaction failed
#                 messages.error(request, 'There was an error saving your profile.')
#                 return redirect(reverse('profile-settings'))

#     else:
#         profile_form = ProfileForm(user=user)
#         link_formset = LinkFormSet(initial=link_data)

#     context = {
#         'profile_form': profile_form,
#         'link_formset': link_formset,
#     }

#     return render(request, 'our_template.html', context)



# #from .forms import IngredientFormSet
# from django.forms.models import modelformset_factory
# from django.shortcuts import render_to_response

# def manage_ingredient(request):
	
# 	context = {
# 		'current_url': resolve(request.path_info).url_name, 
# 		'ingredients': Ingredient.objects.all()}

#     #IngredientFormSet = modelformset_factory(
#     #	Ingredient, fields=('name', 'unit', 'wiki'))
#     #if request.method == 'POST':
#     #    formset = IngredientFormSet(request.POST, request.FILES)
#     #    if formset.is_valid():
#     #        formset.save()
#             # do something.
#     #else:
#     #    formset = IngredientFormSet()
#     #return render_to_response("ingredients/manage_ingredients.html", {
#     #    "formset": formset,
#     #})
# 	return render(request, 'ingredients/manage_ingredients.html', context)