# Generated by Django 2.2.5 on 2020-10-21 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RickAndMorty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='name',
            field=models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Character Name'),
        ),
    ]
