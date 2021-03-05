from django.db import models
from decimal import Decimal

# Create your models here.


class PrimaryBank(models.Model):
    institution = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.institution


class Client(models.Model):
    # Choices
    CLIENT_TYPE_CHOICES = [         #May use later for client or informative details
        ('Buyer', 'Buyer'),
        ('Seller', 'Seller'),
        ('Renter', 'Renter'),
        ('Investor', 'Investor'),
    ]

    # Fields
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    username = models.CharField(max_length=60)
    client_type = models.CharField(max_length=60, choices=CLIENT_TYPE_CHOICES, default='')
    credit_hx = models.CharField(max_length=30, default='')
    primary_bank = models.ForeignKey(PrimaryBank, on_delete=models.CASCADE, blank=True, null=True)
    debt_amount = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))

    # add favorites later

    # the methods
    def __str__(self):
        return self.first_name + " " + self.last_name

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Listing(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('Single Family Home', 'Single Family Home'),
        ('Duplex', 'Duplex'),
        ('Condominium', 'Condominium'),
        ('Commercial', 'Commercial'),
    ]

    name = models.CharField(max_length=255)
    property_type = models.CharField(max_length=60, choices=PROPERTY_TYPE_CHOICES, default='')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




