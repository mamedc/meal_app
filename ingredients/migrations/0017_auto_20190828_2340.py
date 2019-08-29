# Generated by Django 2.2.4 on 2019-08-29 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0016_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.ManyToManyField(related_name='ingredients', to='ingredients.IngredientUnit'),
        ),
    ]
