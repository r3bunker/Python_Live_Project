# Generated by Django 2.2.5 on 2020-09-03 18:16

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('RcanavApp', '0002_auto_20200902_2328'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='savecities',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
