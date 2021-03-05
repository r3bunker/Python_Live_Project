from django.db import models
from datetime import datetime


class Climb(models.Model):

    TYPE_CHOICES = [
        ('Sport', 'Sport'),
        ('Boulder', 'Boulder'),
        ('Trad', 'Trad'),
        ('Alpine', 'Alpine'),
        ('Ice', 'Ice'),
    ]

    ROUTE_GRADE_CHOICES = [

        ('5.7', '5.7'),
        ('5.8', '5.8'),
        ('5.9', '5.9'),
        ('5.10a', '5.10a'), ('5.10b', '5.10b'), ('5.10c', '5.10c'), ('5.10d', '5.10d'),
        ('5.11a', '5.11a'), ('5.11b', '5.11b'), ('5.11c', '5.11c'), ('5.11d', '5.11d'),
        ('5.12a', '5.12a'), ('5.12b', '5.12b'), ('5.12c', '5.12c'), ('5.12d', '5.12d'),
        ('5.13a', '5.13a'), ('5.13b', '5.13b'), ('5.13c', '5.13c'), ('5.13d', '5.13d'),
        ('5.14a', '5.14a'), ('5.14b', '5.14b'), ('5.14c', '5.14c'), ('5.14d', '5.14d'),
        ('5.15a', '5.15a'), ('5.15b', '5.15b'), ('5.15c', '5.15c'), ('5.15d', '5.15d'),

        ('V1', 'V1'), ('V2', 'V2'), ('V3', 'V3'), ('V4', 'V4'), ('V5', 'V5'),
        ('V6', 'V6'), ('V7', 'V7'), ('V8', 'V8'), ('V9', 'V9'), ('V10', 'V10'),
        ('V11', 'V11'), ('V12', 'V12'), ('V13', 'V13'), ('V14', 'V14'), ('V15', 'V15'),

        ('WI1', 'WI1'), ('WI1+', 'WI1+'), ('WI2', 'WI2'), ('WI2+', 'WI2+'),
        ('WI3', 'WI3'), ('WI3+', 'WI3+'), ('WI4', 'WI4'), ('WI4+', 'WI4+'),
        ('WI5', 'WI5'), ('WI5+', 'WI5+'), ('WI6', 'WI6'), ('WI6+', 'WI6+'),
        ('WI7', 'WI7'), ('WI7+', 'WI7+'),
    ]

    ROCK_CHOICES = [
        ('Granite', 'Granite'),
        ('Limestone', 'Limestone'),
        ('Quartzite', 'Quartzite'),
        ('Sandstone', 'Sandstone'),
        ('Cobble', 'Cobble'),
        ('Gneiss', 'Gneiss'),
        ('Unknown', 'Unknown'),
    ]

    name = models.CharField('Name', max_length=40, default='', blank=True, null=False)
    type = models.CharField('Type', max_length=30, default='', blank=True, null=False, choices=TYPE_CHOICES)
    grade = models.CharField('Grade', max_length=20, default='', blank=True, null=False, choices=ROUTE_GRADE_CHOICES)
    pitches = models.PositiveIntegerField('Pitches', default='', blank=True, null=False)
    rock = models.CharField('Rock Type', max_length=40, default='', blank=True, null=False, choices=ROCK_CHOICES)
    image = models.URLField('Image', max_length=255, default='', blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Attempt(models.Model):

    STATUS_CHOICES = [
        ('Onsight', 'Onsight'),
        ('Redpoint', 'Redpoint'),
        ('Pinkpoint', 'Pinkpoint'),
        ('To Do', 'To Do'),
        ('Flash', 'Flash'),
        ('Flail', 'Flail'),
        ('Sent', 'Sent'),
    ]

    LIGHT_CHOICES = [
        ('Shade', 'Shade'),
        ('Sun', 'Sun'),
        ('Night', 'Night'),
    ]

    climb = models.ForeignKey(Climb, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    light = models.CharField(max_length=40, default='', blank=True, null=False, choices=LIGHT_CHOICES)
    temp = models.CharField(max_length=20, default='', null=False)
    shoes = models.CharField(max_length=40, default='', null=False)
    status = models.CharField(max_length=40, default='', blank=True, null=False, choices=STATUS_CHOICES)
    notes = models.CharField(max_length=255, default='', null=True)

    objects = models.Manager()

    class Meta:
        ordering = ['date']
        verbose_name_plural = ['shoes', 'status', 'notes']

    def __str__(self):
        return self.climb.name

