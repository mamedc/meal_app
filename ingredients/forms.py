from django import forms
from .models import IngredientUnit, Ingredient
from django.forms import formset_factory


class IngredientForm(forms.Form):
	name = forms.CharField(max_length=64)
	wiki = forms.URLField(max_length=250)
	unit = forms.ModelMultipleChoiceField(queryset=IngredientUnit.objects.all(), widget=forms.CheckboxSelectMultiple)
	
# class BaseRecipeAddIngrForm(forms.Form):
# 	brec_ingredient_name = forms.ModelChoiceField(queryset=Ingredient.objects.all().order_by('name'), label='brec_ingredients', empty_label='')
# 	brec_ingredient_value = forms.FloatField()
# 	brec_ingredient_unit = forms.ModelChoiceField(queryset=IngredientUnit.objects.all(), empty_label='')

# BaseRecipeAddIngrFormSet = formset_factory(BaseRecipeAddIngrForm, extra=2)

class BaseRecipeForm(forms.Form):
	#name = forms.CharField(label='Base recipe name', max_length=64)
	#brec_yield_value = forms.FloatField()
	#brec_yield_unit = forms.ModelChoiceField(queryset=IngredientUnit.objects.all(), empty_label='')
	#procedure = forms.CharField(widget=forms.Textarea)
	
	# Create sets of ingredient/value/unit fields
	def __init__(self, *args, **kwargs):
		super(BaseRecipeForm, self).__init__(*args, **kwargs)
		self.ingr_sets_counter = 0
		max_ingrs = 3
		for i in range(1, max_ingrs+1):
			self.ingr_sets_counter += 1
			self.fields['brec_ingr_name_%s' % i] = forms.ModelChoiceField(queryset=Ingredient.objects.all().order_by('name'), label='brec_ingredients', empty_label='')
			self.fields['brec_ingr_val_%s' % i] = forms.FloatField()
			self.fields['brec_ingr_unit_%s' % i] = forms.ModelChoiceField(queryset=IngredientUnit.objects.all(), empty_label='')
	



# class IngredientUnitForm(forms.ModelForm):
#     class Meta:
#         model = IngredientUnit
#         fields = ['unitName', 'unitSymbol']


# class IngredientForm(forms.ModelForm):
#     class Meta:
#         model = Ingredient
#         fields = ['name', 'unit', 'wiki']






#class RecipeForm(forms.Form):
#	name = forms.CharField()
#	recipe_yield = forms.IntegerField()
#	recipeIngredients = forms.ModelMultipleChoiceField(Ingredient.objects.all())




# class RecipeForm(forms.Form):
#     name = forms.CharField()
#     recipe_yield = forms.IntegerField()
#     extra_field_count = forms.CharField(widget=forms.HiddenInput())

#     def __init__(self, *args, **kwargs):
#         extra_fields = kwargs.pop('extra', 0)

#         super(RecipeForm, self).__init__(*args, **kwargs)
#         self.fields['extra_field_count'].initial = extra_fields

#         for index in range(int(extra_fields)):
#             # generate extra fields in the number specified via extra_fields
#             self.fields['extra_field_{index}'.format(index=index)] = forms.CharField()



# class LinkForm(forms.Form):
    
#     anchor = forms.CharField(
#                     max_length=100,
#                     widget=forms.TextInput(attrs={
#                         'placeholder': 'Link Name / Anchor Text',
#                     }),
#                     required=False)
    
#     url = forms.URLField(
#                     widget=forms.URLInput(attrs={
#                         'placeholder': 'URL',
#                     }),
#                     required=False)



# class ProfileForm(forms.Form):
#     """
#     Form for user to update their own profile details
#     (excluding links which are handled by a separate formset)
#     """
#     def __init__(self, *args, **kwargs):
        
#         self.user = kwargs.pop('user', None)
        
#         super(ProfileForm, self).__init__(*args, **kwargs)

#         self.fields['first_name'] = forms.CharField(
#                                         max_length=30,
#                                         initial = self.user.first_name,
#                                         widget=forms.TextInput(attrs={
#                                             'placeholder': 'First Name',
#                                         }))
        
#         self.fields['last_name'] = forms.CharField(
#                                         max_length=30,
#                                         initial = self.user.last_name,
#                                         widget=forms.TextInput(attrs={
#                                             'placeholder': 'Last Name',
#                                         }))


# from django.forms.formsets import BaseFormSet

# class BaseLinkFormSet(BaseFormSet):
#     def clean(self):
#         """
#         Adds validation to check that no two links have the same anchor or URL
#         and that all links have both an anchor and URL.
#         """
#         if any(self.errors):
#             return

#         anchors = []
#         urls = []
#         duplicates = False

#         for form in self.forms:
#             if form.cleaned_data:
#                 anchor = form.cleaned_data['anchor']
#                 url = form.cleaned_data['url']

#                 # Check that no two links have the same anchor or URL
#                 if anchor and url:
#                     if anchor in anchors:
#                         duplicates = True
#                     anchors.append(anchor)

#                     if url in urls:
#                         duplicates = True
#                     urls.append(url)

#                 if duplicates:
#                     raise forms.ValidationError(
#                         'Links must have unique anchors and URLs.',
#                         code='duplicate_links'
#                     )

#                 # Check that all links have both an anchor and URL
#                 if url and not anchor:
#                     raise forms.ValidationError(
#                         'All links must have an anchor.',
#                         code='missing_anchor'
#                     )
#                 elif anchor and not url:
#                     raise forms.ValidationError(
#                         'All links must have a URL.',
#                         code='missing_URL'
#                     )


# #class IngredientForm(forms.Form):
# #	name = forms.CharField()
# #	unit = forms.DateField()


# from django.forms.models import modelformset_factory
# from .models import Ingredient
# IngredientFormSet = modelformset_factory(Ingredient, fields=('name', 'unit', 'wiki'))