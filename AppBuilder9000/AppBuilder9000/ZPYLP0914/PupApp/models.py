from django.db import models
from django.forms import ModelForm

class OwnerManager(models.Manager):
    pass

class Owner(models.Model):
    owner_fname = models.CharField('First Name', max_length=50, blank=False, null=False)
    owner_lname = models.CharField('Last Name',max_length=50, blank=False, null=False)
    owner_zipcode= models.CharField('Zip Code',max_length=10, blank=False, null=False)
    owner_phone = models.IntegerField('Phone Number',blank=False, null=False)
    owner_email = models.EmailField('Email',max_length=50, blank=False, null=False)

    Owner=models.Manager()

    def __str__(self):
        return self.owner_email

SIZE_CHOICES = [
    ('XS', 'Tiny (under 10lbs)',),
    ('S', 'Small (10-20lbs)'),
    ('M', 'Medium (20-40lbs)'),
    ('L', 'Large (40-60lbs)'),
    ('XL', 'XLarge (over 60lbs)'),
]

PLAYTYPE_CHOICES = [
    ('Gentle', 'Gentle',),
    ('Medium', 'Medium'),
    ('Rowdy', 'Rowdy'),
]

PLAYPLACE_CHOICES = [
    ('Park', 'Park'),
    ('Water', 'Water'),
]

class PlayTimeManager(models.Manager):
    pass

class PlayTime(models.Model):
    dog_name = models.CharField(max_length=50, blank=False)
    age = models.IntegerField(blank=False,  null=True)
    breed = models.CharField(max_length=50, blank=False)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES, blank=False)
    play_type = models.CharField(max_length=50, choices=PLAYTYPE_CHOICES, blank=False)
    play_place = models.CharField(max_length=50, choices=PLAYPLACE_CHOICES, blank=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=False, null=False)

    PlayTime=models.Manager()

    def __str__(self):
        return self.dog_name

