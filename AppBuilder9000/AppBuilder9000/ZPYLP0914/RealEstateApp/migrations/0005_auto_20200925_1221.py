# Generated by Django 2.2.5 on 2020-09-25 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RealEstateApp', '0004_client_primary_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='primary_bank',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RealEstateApp.PrimaryBank'),
        ),
    ]