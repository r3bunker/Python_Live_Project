# Generated by Django 2.2.5 on 2020-07-06 23:31

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('SFReview', '0002_auto_20200702_1723'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='bookreview',
            managers=[
                ('reviews', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='bookreview',
            name='Author',
            field=models.CharField(choices=[('sbrust', 'Steven Brust'), ('bsanderson', 'Brandon Sanderson'), ('pkd', 'Philip K Dick'), ('lmbujold', 'Lois McMasters Bujold')], default='pkd', max_length=80),
        ),
    ]
