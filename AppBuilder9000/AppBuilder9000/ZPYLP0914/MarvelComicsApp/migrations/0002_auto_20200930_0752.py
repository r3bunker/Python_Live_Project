# Generated by Django 2.2.5 on 2020-09-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarvelComicsApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CharacterFamiliarity',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='username',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='sub_username',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
