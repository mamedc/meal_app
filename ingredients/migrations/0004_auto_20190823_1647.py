# Generated by Django 2.2.4 on 2019-08-23 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0003_auto_20190823_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='recipes',
        ),
        migrations.CreateModel(
            name='IngrQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('ingr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredients.Ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredients.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipeIngredients',
            field=models.ManyToManyField(through='ingredients.IngrQuantity', to='ingredients.Ingredient'),
        ),
    ]
