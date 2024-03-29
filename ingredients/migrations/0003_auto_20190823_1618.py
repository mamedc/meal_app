# Generated by Django 2.2.4 on 2019-08-23 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0002_ingredient_wiki'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('recipe_yield', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipes',
            field=models.ManyToManyField(blank=True, related_name='ingredients', to='ingredients.Recipe'),
        ),
    ]
