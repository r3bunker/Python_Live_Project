from django.db import models


class FishKeepingUser(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=30, blank=False)

    Accounts = models.Manager()

    def __str__(self):
        return self.first_name + " " + self.last_name


FISH_TYPE = [
    ('Freshwater', 'Freshwater'),
    ('Brackish', 'Brackish'),
    ('Saltwater', 'Saltwater'),
]


class FishWishList(models.Model):
    fish_type = models.CharField(max_length=10, choices=FISH_TYPE, null=True)
    name = models.CharField(max_length=50, default="", blank=False)
    notes = models.TextField(max_length=300, default="", blank=True)
    budget = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
    image = models.URLField(max_length=255, default="", blank=True)
    account = models.ForeignKey(FishKeepingUser, on_delete=models.CASCADE)

    Fish = models.Manager()

    def __str__(self):
        return self.name
