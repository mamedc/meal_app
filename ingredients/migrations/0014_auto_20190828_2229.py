# Generated by Django 2.2.4 on 2019-08-29 01:29

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('ingredients', '0013_auto_20190828_2011'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredient_Unit',
            new_name='IngredientUnit',
        ),
        migrations.RemoveField(
            model_name='baserecipe',
            name='recipeIngredients',
        ),
        migrations.RemoveField(
            model_name='baserecipe',
            name='yield_unit',
        ),
        migrations.RemoveField(
            model_name='baserecipequantity',
            name='baserecipe',
        ),
        migrations.RemoveField(
            model_name='baserecipequantity',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='ingrquantity',
            name='ingr',
        ),
        migrations.RemoveField(
            model_name='ingrquantity',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='recipeBaseRecipes',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='recipeIngredients',
        ),
        migrations.DeleteModel(
            name='BaseIngrQuantity',
        ),
        migrations.DeleteModel(
            name='BaseRecipe',
        ),
        migrations.DeleteModel(
            name='BaseRecipeQuantity',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='IngrQuantity',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]