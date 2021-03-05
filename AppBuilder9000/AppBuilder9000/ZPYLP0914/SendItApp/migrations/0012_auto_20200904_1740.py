# Generated by Django 2.2.5 on 2020-09-04 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SendItApp', '0011_auto_20200904_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boulder',
            name='rock',
            field=models.CharField(choices=[('Limestone', 'Limestone'), ('Sandstone', 'Sandstone'), ('Granite', 'Granite'), ('Unknown', 'Unknown'), ('Quartzite', 'Quartzite')], default='Unknown', max_length=40),
        ),
        migrations.AlterField(
            model_name='boulder',
            name='status',
            field=models.CharField(choices=[('Flash', 'Flash'), ('To Do', 'To Do'), ('In Progress', 'In Progress')], default='Flash', max_length=40),
        ),
        migrations.AlterField(
            model_name='sport',
            name='rock',
            field=models.CharField(choices=[('Limestone', 'Limestone'), ('Sandstone', 'Sandstone'), ('Granite', 'Granite'), ('Unknown', 'Unknown'), ('Quartzite', 'Quartzite'), ('Cobble', 'Cobble')], default='Unknown', max_length=40),
        ),
        migrations.AlterField(
            model_name='sport',
            name='status',
            field=models.CharField(choices=[('Flail', 'Flail'), ('Pinkpoint', 'Pinkpoint'), ('Flash', 'Flash'), ('To Do', 'To Do'), ('Redpoint', 'Redpoint'), ('Onsight', 'Onsight')], default='To Do', max_length=40),
        ),
    ]
