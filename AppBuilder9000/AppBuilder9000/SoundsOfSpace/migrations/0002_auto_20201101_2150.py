# Generated by Django 2.2.5 on 2020-11-02 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SoundsOfSpace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='atmosphere',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Atmosphere'),
        ),
        migrations.AlterField(
            model_name='planet',
            name='planet_key',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Musical Key'),
        ),
    ]