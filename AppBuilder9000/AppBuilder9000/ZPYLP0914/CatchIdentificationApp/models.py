from django.db import models

BOOL_CHOICES= [
    (True, 'Boat'),
    (False, 'Bank'),
]


class TheContact(models.Model):
    fishing_Name = models.CharField(max_length=30, blank=True, null=False)
    first_Name = models.CharField(max_length=30, blank=False, null=False)
    last_Name = models.CharField(max_length=30, blank=False, null=False)
    emailAddress = models.EmailField(max_length=60, blank=False, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.first_Name


class TheBigOne(models.Model):
    fishing_Name = models.ForeignKey(TheContact, on_delete=models.CASCADE)
    fish_Type = models.CharField(max_length=30, blank=True, null=False)
    fish_Length = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=False)
    fish_Weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=False)
    body_of_Water = models.CharField(max_length=60, blank=True, null=False)
    tackle_Used = models.CharField(max_length=30, blank=False, null=False)
    boatOrBank = models.BooleanField(verbose_name="Boat or Bank Fishing?", choices=BOOL_CHOICES, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.fish_Type
