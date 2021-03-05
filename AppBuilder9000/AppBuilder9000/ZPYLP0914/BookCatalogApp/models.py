from django.db import models
from datetime import datetime

class Book(models.Model):
    TYPE_CHOICES = (
        ('hardback', 'Hardback'),
        ('paperback', 'Paperback'),
        ('kindle', 'Kindle'),
        ('epub', 'Epub'),
        ('pdf', 'PDF'),
    )
    id = models.IntegerField(primary_key=True)
    bk_title = models.CharField(max_length=100, default="", blank=True, null=False)
    bk_author = models.CharField(max_length=60, default="", blank=True, null=False)
    bk_pub_date = models.DateField(default=datetime.now)
    bk_series = models.CharField(max_length=100, default="", blank=True)
    bk_type = models.CharField(max_length=15, default="", choices=TYPE_CHOICES)
    bk_purchase_date = models.DateField(default=datetime.now)
    bk_price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    books = models.Manager()

    def __str__(self):
        return "{self.bk_author} : {self.bk_title}"
