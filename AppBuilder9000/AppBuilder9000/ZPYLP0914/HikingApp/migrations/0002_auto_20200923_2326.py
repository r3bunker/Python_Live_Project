# Generated by Django 2.2.5 on 2020-09-24 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HikingApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hike_preferences',
            name='favorite_types_of_hikes',
            field=models.CharField(choices=[('Flat', 'Flat'), ('Hilly', 'Hilly'), ('Mountains', 'Mountains'), ('Rivers', 'Rivers'), ('Glacier', 'Glacier'), ('Lake', 'Lake')], max_length=30),
        ),
        migrations.AlterField(
            model_name='hike_preferences',
            name='how_healthy_are_you',
            field=models.CharField(choices=[('Not to Healthy', 'Not to Healthy'), ('Somewhat Healthy', 'Somewhat Healthy'), ('Healthy', 'Healthy'), ('Pretty Healthy', 'Pretty Healthy'), ('Very Healthy', 'Very Healthy')], max_length=30),
        ),
        migrations.AlterField(
            model_name='hike_preferences',
            name='perfect_length_of_hike',
            field=models.CharField(choices=[('1-2 Miles', '1-2 Miles'), ('2-5 Miles,', '2-5 Miles'), ('5-8 Miles', '5-8 Miles'), ('8-10 Miles', '8-10 Miles'), ('10+ Miles', '10+ Miles')], max_length=30),
        ),
    ]
