# Generated by Django 2.2.4 on 2019-08-29 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0017_auto_20190828_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseRec_Ingredient_Amount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='BaseRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('brec_yield_value', models.FloatField()),
                ('procedure', models.TextField()),
                ('brec_ingredients', models.ManyToManyField(related_name='baseRecipes', through='ingredients.BaseRec_Ingredient_Amount', to='ingredients.Ingredient')),
                ('brec_yield_unit', models.ManyToManyField(related_name='baseRecipes', to='ingredients.IngredientUnit')),
            ],
        ),
        migrations.AddField(
            model_name='baserec_ingredient_amount',
            name='baseRecipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ingredient_amount', to='ingredients.BaseRecipe'),
        ),
        migrations.AddField(
            model_name='baserec_ingredient_amount',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ingredient_amount', to='ingredients.Ingredient'),
        ),
    ]