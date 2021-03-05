from datetime import date
from django.db import models

# Create your models here.
RATING_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]

class FestivalReview(models.Model):
    review_date = models.DateField(verbose_name="today's date", auto_now_add=True)
    first_name = models.CharField(verbose_name="reviewer name", default="Anonymous", max_length=50, blank=True)
    festival_title = models.CharField(max_length=200)
    comment = models.TextField(max_length=1000, default="", blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES)

    reviews = models.Manager()

    def __str__(self):
        return self.festival_title

# class USCities(models.Model):
#     city = models.CharField(max_length=70)
#     lat = models.DecimalField(max_digits=20, decimal_places=20)
#     lng = models.DecimalField(max_digits=20, decimal_places=20)
#     country = models.CharField(max_length=2)
#     state = models.CharField(max_length=50)
#
#     cities = models.Manager()
#
#     def __str__(self):
#         return self.city

# class USCities(models.Model):
#     city = models.CharField(max_length=70)
#     lat = models.FloatField()
#     lng = models.FloatField()
#     country = models.CharField(max_length=2)
#     state = models.CharField(max_length=50)
#
#     cities = models.Manager()
#
#     def __str__(self):
#         return self.city

class USCities(models.Model):
    city = models.CharField(max_length=70)
    lat = models.FloatField()
    lng = models.FloatField()
    country = models.CharField(max_length=2)
    state = models.CharField(max_length=50)
    state_code = models.CharField(max_length=2)

    cities = models.Manager()

    def __str__(self):
        return self.city