from django.db import models
from datetime import datetime

# Create your models here.

TYPE_CHOICES = (
    ('Action', 'Action'),
    ('Comedy', 'Comedy'),
    ('Drama', 'Drama'),
    ('Horror', 'Horror'),
)



class Movie(models.Model):
    genre = models.CharField(max_length=60, choices=TYPE_CHOICES)
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    description =models.CharField(max_length=60, default="", blank=True, null=False)
    release_date= models.DateField(default=datetime.now)

    objects = models.Manager()

    def __str__(self):
        return self.title
