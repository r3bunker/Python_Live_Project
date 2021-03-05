from django.db import models

#popular cities
cities=[
  ("Bangui", "Bangui"),
  ("Bouar", "Bouar"),
  ("Boali", "Boali"),
  ("Ouadda","Ouadda"),
  ("Baboua", "Baboua"),
]


# Create your models here.
class savecities(models.Model):
  cities_name = models.CharField(max_length=75, blank=False, choices=cities)
  reason = models.CharField(max_length=200, blank=False)
  date_saved = models.DateField()
  Rate_cities = models.DecimalField(default=0.00, max_digits=100, decimal_places=4)

#return cities name
  def __str__(self):
    return self.cities_name


  objects = models.Manager()