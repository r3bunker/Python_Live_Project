from datetime import datetime
from django.db import models

RATING_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
]


class ComicUser(models.Model):
    username = models.CharField(default="", max_length=255, unique=True, blank=False, null=False)
    email = models.EmailField(default="", max_length=255, unique=True, blank=False, null=False)
    birth_date = models.DateField(default="", verbose_name="Date of Birth")
    password = models.CharField(default="", max_length=255, blank=False, null=False)
    created = models.DateTimeField(default="")
    modified = models.DateTimeField(default="")
    users = models.Manager()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.now()
        self.modified = datetime.now()
        return super(ComicUser, self).save(*args, **kwargs)


class ComicReview(models.Model):
    series = models.CharField(default="", max_length=255, blank=False, null=False)
    issue = models.CharField(default="", max_length=255, blank=False, null=False)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, blank=False, null=False)
    review = models.TextField(default="", blank=False, null=False)
    created = models.DateTimeField(default="")
    modified = models.DateTimeField(default="")
    user = models.ForeignKey(ComicUser, on_delete=models.CASCADE)
    reviews = models.Manager()

    def __str__(self):
        return "I rate " + self.series + " " + self.issue + " a " + self.rating + " out of 10."

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.now()
        self.modified = datetime.now()
        return super(ComicReview, self).save(*args, **kwargs)
