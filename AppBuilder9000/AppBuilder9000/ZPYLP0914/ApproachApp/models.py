from django.db import models
from .managers import ItemsViewer

# Create your models here.


# Creates a user
class ApproachUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=75)

    info = models.Manager()

    def __str__(self):
        return self.first_name + " " + self.last_name


climb_type = [('T', 'Trad'), ('S', 'Sport'), ('B', 'Bouldering'), ('M', 'Mixed'), ('I', 'Ice')]


class Climb(models.Model):
    account = models.ForeignKey(ApproachUser, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    climbing_area = models.CharField(max_length=50)
    climbing_wall = models.CharField(max_length=50)
    climb_type = models.CharField(max_length=15, choices=climb_type)
    climb_grade = models.CharField(max_length=5)
    climb_name = models.CharField(max_length=75)
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.climb_name + " " + self.climb_grade

    info = models.Manager()
    view = ItemsViewer()


class TripManager(models.Model):
    trip_name = models.CharField(max_length=254, unique=True)
    trip_description = models.TextField(max_length=500)
    budget = models.DecimalField(max_digits=15, decimal_places=2)
    transportation = models.CharField(max_length=25)
    shelter_type = models.CharField(max_length=50)
    climbs = models.ManyToManyField(Climb, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    people = models.ManyToManyField(ApproachUser)

    info = models.Manager()
    view = ItemsViewer()

    def __str__(self):
        return self.trip_name


class Guidebook(models.Model):
    name = models.CharField(max_length=254, unique=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    publisher = models.CharField(max_length=100)
    publishing_date = models.DateField()
    climb_area = models.CharField(max_length=50)
    #image = models.ImageField(blank=True, null=True, upload_to='images/ApproachApp/', max_length=255)

    def __str__(self):
        return self.name

    info = models.Manager()
    view = ItemsViewer()
