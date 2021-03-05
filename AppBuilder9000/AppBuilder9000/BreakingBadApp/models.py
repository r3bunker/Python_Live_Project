from django.db import models


class Episode(models.Model):
    episode_title = models.CharField(max_length=50)
    episode_season = models.IntegerField()
    episode_number = models.IntegerField()
    episode_date = models.DateField()

    Episodes = models.Manager()

    def __str__(self):
        return self.episode_title

