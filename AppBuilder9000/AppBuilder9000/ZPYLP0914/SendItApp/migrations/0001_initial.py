# Generated by Django 2.2.5 on 2020-09-04 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('grade', models.CharField(default=0.0, max_length=20)),
                ('type', models.CharField(choices=[('Sport', 'Sport'), ('Alpine', 'Alpine'), ('Boulder', 'Boulder'), ('Trad', 'Trad'), ('Ice', 'Ice')], max_length=40)),
                ('pitches', models.DecimalField(blank=True, decimal_places=0, default='', max_digits=2, null=True)),
                ('status', models.CharField(choices=[('Flail', 'Flail'), ('ToDo', 'ToDo'), ('Onsight', 'Onsight'), ('Redpoint', 'Redpoint'), ('Flash', 'Flash'), ('Pinkpoint', 'Pinkpoint'), ('Blackpoint', 'Blackpoint')], max_length=40)),
                ('image', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
    ]