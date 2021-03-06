# Generated by Django 2.2.5 on 2020-10-05 15:43

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MarvelComicsApp', '0010_delete_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_username', models.CharField(default='', max_length=50, unique=True, verbose_name='Username')),
                ('sub_email', models.EmailField(max_length=50, verbose_name='Email')),
                ('sub_fname', models.CharField(max_length=50, verbose_name='First Name')),
                ('sub_lname', models.CharField(max_length=50, verbose_name='Last Name')),
                ('sub_dob', models.DateField(max_length=20, verbose_name='Date of Birth')),
                ('sub_team', models.CharField(choices=[('The Avengers', 'The Avengers'), ('The X-Men', 'The X-Men'), ('Inhumans', 'Inhumans'), ('Fantastic 4', 'Fantastic 4'), ('Guardians of the Galaxy', 'Guardians of the Galaxy'), ('Other', 'Other')], default='', max_length=50, verbose_name='What is your favorite super team?')),
                ('sub_preference', models.BooleanField(default=True, verbose_name='Do you prefer to read comics online?')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
