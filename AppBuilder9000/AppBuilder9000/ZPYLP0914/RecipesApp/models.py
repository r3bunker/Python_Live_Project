from django.db import models


CHOICES =[
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Snack', 'Snack'),
]


class Recipe(models.Model):
    Title = models.CharField(max_length=30, default="")
    Type = models.CharField(max_length=30, choices=CHOICES)
    Ingredients = models.TextField(max_length=300, default="")
    Directions = models.TextField(max_length=400, default="")

    object = models.Manager()

    def __str__(self):
        return self.Title
