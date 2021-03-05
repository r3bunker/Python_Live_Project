from django.db import models

#Create Model
POS_CHOICES = [
    ('Forward', 'Forward'),
    ('Midfielder', 'Midfielder'),
    ('Defender', 'Defender'),
    ('Goalkeeper', 'Goalkeeper'),
]


class player(models.Model):
    Name = models.CharField(max_length=50, default="")
    Position = models.CharField(max_length=10, choices=POS_CHOICES, default="")
    Team = models.CharField(max_length=60, default="")
    Salary = models.IntegerField(default="")

    objects = models.Manager()

    def __str__(self):
        return self.Name
