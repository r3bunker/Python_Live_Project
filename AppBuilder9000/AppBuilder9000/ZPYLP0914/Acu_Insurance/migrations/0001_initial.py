# Generated by Django 2.2.5 on 2020-10-15 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_name', models.CharField(blank=True, default='', max_length=60)),
                ('first_name', models.CharField(blank=True, default='', max_length=30)),
                ('last_name', models.CharField(blank=True, default='', max_length=30)),
                ('specialty', models.CharField(blank=True, default='', max_length=30)),
                ('street_address', models.CharField(blank=True, default='', max_length=100)),
                ('city_name', models.CharField(blank=True, default='', max_length=60)),
                ('zip_code', models.CharField(blank=True, default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_name', models.CharField(blank=True, default='', max_length=30)),
                ('copay', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('percent_covered', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('deductible', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('clinic_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Acu_Insurance.Acu')),
            ],
        ),
    ]
