# Generated by Django 2.2.5 on 2020-10-21 07:02

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('FestivalApp', '0014_auto_20201020_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='US_Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=70)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('country', models.CharField(max_length=2)),
                ('state', models.CharField(max_length=50)),
                ('state_code', models.CharField(max_length=2)),
            ],
            managers=[
                ('cities', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='USCities',
        ),
    ]
