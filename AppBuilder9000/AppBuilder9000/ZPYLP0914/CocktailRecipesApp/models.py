from django.db import models


class Cocktail(models.Model):
    name = models.CharField(max_length=60, verbose_name="Cocktail Name", default="", blank=False, null=False)
    ingredient1 = models.CharField(max_length=60, verbose_name="Ingredient", default="", blank=False, null=False)
    ingredient2 = models.CharField(max_length=60, verbose_name="Ingredient", default="", blank=False, null=False)
    ingredient3 = models.CharField(max_length=60, verbose_name="Ingredient", default="", blank=True, null=True)
    ingredient4 = models.CharField(max_length=60, verbose_name="Ingredient", default="", blank=True, null=True)
    ingredient5 = models.CharField(max_length=60, verbose_name="Ingredient", default="", blank=True, null=True)
    ingredient6 = models.CharField(max_length=60, verbose_name="Ingredient", default="", blank=True, null=True)
    ingredient7 = models.CharField(max_length=60, verbose_name="Ingredient", default="", blank=True, null=True)
    ingredient8 = models.CharField(max_length=60, verbose_name="Ingredient", default="", blank=True, null=True)
    ingredient9 = models.CharField(max_length=60, verbose_name="Ingredient", default="", blank=True, null=True)
    ingredient10 = models.CharField(max_length=60, verbose_name="Ingredient", default="", blank=True, null=True)
    ingredient11 = models.CharField(max_length=60, verbose_name="Ingredient", default="", blank=True, null=True)
    ingredient12 = models.CharField(max_length=60, verbose_name="Ingredient", default="", blank=True, null=True)
    ingredient13 = models.CharField(max_length=60, verbose_name="Ingredient", default="", blank=True, null=True)
    ingredient14 = models.CharField(max_length=60, verbose_name="Ingredient", default="", blank=True, null=True)
    ingredient15 = models.CharField(max_length=60, verbose_name="Ingredient", default="", blank=True, null=True)
    instructions = models.CharField(max_length=10000, default="", blank=False, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.name
