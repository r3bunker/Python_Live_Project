from django.db import models



# Create your models here.


SCORE_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]

class BookReview(models.Model):
    Author = models.CharField(max_length=50, blank=False)
    Title = models.CharField(max_length=100, blank=False)
    Review = models.TextField(max_length=1000, default="", blank=True)
    Score = models.IntegerField(choices=SCORE_CHOICES)

    reviews = models.Manager()

    def __str__(self):
        return self.Title
