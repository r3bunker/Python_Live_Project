# Generated by Django 2.2.5 on 2020-09-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NSW_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateField(blank=True, db_column='release_date', null=True, verbose_name='Release Date'),
        ),
    ]
