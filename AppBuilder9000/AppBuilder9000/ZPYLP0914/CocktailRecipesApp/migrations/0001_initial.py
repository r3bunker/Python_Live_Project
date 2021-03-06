# Generated by Django 2.2.5 on 2020-09-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60, verbose_name='Cocktail Name')),
                ('ingredient1', models.CharField(default='', max_length=60, verbose_name='Ingredient')),
                ('ingredient2', models.CharField(default='', max_length=60, verbose_name='Ingredient')),
                ('ingredient3', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Ingredient')),
                ('ingredient4', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Ingredient')),
                ('ingredient5', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Ingredient')),
                ('ingredient6', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Ingredient')),
                ('ingredient7', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Ingredient')),
                ('ingredient8', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Ingredient')),
                ('ingredient9', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Ingredient')),
                ('ingredient10', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Ingredient')),
                ('ingredient11', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Ingredient')),
                ('ingredient12', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Ingredient')),
                ('ingredient13', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Ingredient')),
                ('ingredient14', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Ingredient')),
                ('ingredient15', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Ingredient')),
                ('instructions', models.CharField(default='', max_length=10000)),
            ],
        ),
    ]
