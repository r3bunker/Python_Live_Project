from django.db import models
#  rating_choices for ratings using an integer for the field
RATING_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]

class SurfSpot(models.Model):
    spotName = models.CharField(max_length=50, verbose_name="Surf Spot Name", default="", null=False)
    location = models.CharField(max_length=80, verbose_name="County/State", default="", null=False)
    description = models.TextField(max_length=300, verbose_name="Your Description", default="", blank=True)
    rating = models.IntegerField(verbose_name="Your Rating", choices=RATING_CHOICES, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.spotName

