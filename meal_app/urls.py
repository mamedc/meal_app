"""meal_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from ingredients import views as ingrs_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    
    path('ingredients/', ingrs_views.ingredients, name='ingredients-page'),
    path('ingredient/<int:ingredient_id>', ingrs_views.ingredient, name='ingredient-page'),
    path('recipes/', ingrs_views.recipes, name='recipes-page'),
    path('recipe/<int:recipe_id>', ingrs_views.recipe, name='recipe-page'),
    path('recipes/add_recipe/', ingrs_views.add_recipe_page, name='add_recipe-page'),
    path('recipes/add_recipe_submit/', ingrs_views.add_recipe_submit, name='add_recipe_submit-page'),

    path('register/', user_views.register, name='register-page'),
]
