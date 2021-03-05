from django.db import models


PRICE_CHOICES = [
    (1,'$'),
    (2,'$$'),
    (3,'$$$'),
    (4,'$$$$'),
]


class Restaurant(models.Model):
    zomatoID = models.IntegerField(verbose_name="Zomato ID", blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name="Restaurant Name", default="", blank=False, null=False)
    url = models.URLField(max_length=200, verbose_name="Link to Zomato page", blank=True, null=True)
    img = models.URLField(max_length=200, verbose_name="Image link", blank=True, null=True)
    address = models.CharField(max_length=255, default="", blank=False, null=False)
    latitude = models.FloatField(max_length=10, verbose_name="Latitude", blank=True, null=True)
    longitude = models.FloatField(max_length=10, verbose_name="Longitude", blank=True, null=True)
    cuisines = models.CharField(max_length=255, default="", blank=True)
    hours = models.CharField(max_length=255, default="", blank=True)
    avgfortwo = models.IntegerField(verbose_name="Average for two", blank=True, null=True)
    pricerange = models.IntegerField(verbose_name="Price range", choices=PRICE_CHOICES, blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="Rating", blank=True, null=True)
    rating_text = models.CharField(max_length=50, default="", verbose_name="Described as", blank=True)
    votes = models.IntegerField(verbose_name="Number of votes", blank=True, null=True)
    menu = models.URLField(max_length=200, verbose_name="Link to menu", blank=True, null=True)
    phone = models.CharField(max_length=100, default="", verbose_name="Phone number(s)", blank=True)
    establishment = models.CharField(max_length=255, default="", verbose_name="Type", blank=True)
    takeaway = models.BooleanField(verbose_name="Takeaway", blank=True, null=True)
    delivery = models.BooleanField(verbose_name="Delivery", blank=True, null=True)
    vegetarian = models.BooleanField(verbose_name="Vegetarian Options", blank=True, null=True)
    vegan = models.BooleanField(verbose_name="Vegan Options", blank=True, null=True)
    gluten_free = models.BooleanField(verbose_name="Gluten Free Options", blank=True, null=True)
    user_rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="MyRating", blank=True, null=True)
    user_comments = models.TextField(max_length=500, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name
