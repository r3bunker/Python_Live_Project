from django.db import models


class Acu(models.Model):
    clinic_name = models.CharField(max_length=60, default="")
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
    specialty = models.CharField(max_length=30, default="")
    street_address = models.CharField(max_length=100, default="")
    city_name = models.CharField(max_length=60, default="")
    zip_code = models.CharField(max_length=30, default="")

    objects = models.Manager()

    def __str__(self):
        return self.clinic_name


class Insurance(models.Model):
    clinic_name = models.ForeignKey(Acu, on_delete=models.CASCADE)
    insurance_name = models.CharField(max_length=30, default="")
    copay = models.DecimalField(max_digits=5, decimal_places=2, default="")
    percent_covered = models.DecimalField(max_digits=5, decimal_places=2, default="")
    deductible = models.DecimalField(max_digits=10, decimal_places=2, default="")

    objects = models.Manager()

    def __str__(self):
        return self.insurance_name

# Create your models here.
