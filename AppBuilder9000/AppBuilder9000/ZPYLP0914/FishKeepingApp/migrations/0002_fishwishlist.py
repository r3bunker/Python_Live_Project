# Generated by Django 2.2.5 on 2020-09-11 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FishKeepingApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FishWishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fish_type', models.CharField(choices=[('FR', 'Freshwater'), ('BR', 'Brackish'), ('SA', 'Saltwater')], max_length=2, null=True)),
                ('name', models.CharField(default='', max_length=50)),
                ('notes', models.TextField(blank=True, default='', max_length=300)),
                ('budget', models.DecimalField(decimal_places=2, default=0.0, max_digits=10000)),
                ('image', models.CharField(blank=True, default='', max_length=255)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FishKeepingApp.FishKeepingUser')),
            ],
        ),
    ]
