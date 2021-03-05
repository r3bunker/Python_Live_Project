from django.db import models
from django import forms

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    Users = models.Manager()


class Movie(models.Model):
    title = models.CharField(max_length=50)

    Movies = models.Manager()