# Generated by Django 2.2.5 on 2020-09-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='delivery',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Delivery?'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='outdoor_seating',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Outdoor seating/area?'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='take_out',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Take-out?'),
        ),
    ]
