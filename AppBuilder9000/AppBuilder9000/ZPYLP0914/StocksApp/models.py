from django.db import models


# adds ticker for user input
class Stock(models.Model):
    ticker = models.CharField(max_length=20)

    def __str__(self):
        return self.ticker
