from django.db import models
from django import forms


# Create your models here.
class sighting(models.Model):
    Pokemon_Name = models.CharField(max_length=50)
    Pokemon_Number = models.IntegerField()
    Pokemon_Date = models.DateField(max_length=20)
    Pokemon_notes = models.CharField(max_length=300)

    Sightings = models.Manager()
    # Pokemon_image = models.ImageField
    def __str__(self):
        return self.id


class Noteq(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(Pokemon_notes='')
