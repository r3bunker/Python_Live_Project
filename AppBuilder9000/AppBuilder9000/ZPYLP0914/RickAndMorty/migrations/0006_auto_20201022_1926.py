# Generated by Django 2.2.5 on 2020-10-22 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RickAndMorty', '0005_auto_20201022_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characters',
            name='description',
        ),
        migrations.AddField(
            model_name='characters',
            name='image',
            field=models.CharField(default='', max_length=300, verbose_name='Character Image'),
        ),
    ]
