from django.db import models

# Create your models here.
ALIGNMENT_CHOICES = [
    ('Good', 'Good'),
    ('Evil', 'Evil'),
    ('Neutral', 'Neutral'),
]

class Characters(models.Model):
    name = models.CharField(max_length=60, verbose_name="Character Name")
    alignment = models.CharField(max_length=10, verbose_name="Character Alignment", choices=ALIGNMENT_CHOICES, null=False)
    catchPhrase = models.CharField(max_length=150, verbose_name="Character Catch Phrase", default="")
    image = models.CharField(max_length=300, verbose_name="Image URL", default="")
    description = models.CharField(max_length=450, verbose_name="Character Description", default="")

    objects = models.Manager()

    def __str__(self):
        return self.name
