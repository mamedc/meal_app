# Generated by Django 2.2.4 on 2019-08-28 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0006_auto_20190823_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='ingredient_unit',
            name='unit',
            field=models.CharField(max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipeIngredients',
            field=models.ManyToManyField(related_name='rec_ingredients', through='ingredients.IngrQuantity', to='ingredients.Ingredient'),
        ),
    ]
