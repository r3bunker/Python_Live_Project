from django.db import models

class ParksInformation(models.Model):
    TodaysDate = models.DateField(blank=True, null=True)
    UsersName = models.CharField(max_length=60, default='')
    ParkName = models.CharField(max_length=60, default='')
    Comments = models.CharField(max_length=300, default='')


    objects = models.Manager()

    def __str__(self):
        return self.ParkName