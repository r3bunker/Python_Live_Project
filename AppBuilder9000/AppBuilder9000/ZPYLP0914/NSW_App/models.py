from django.db import models

USER_RATINGS = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]

ESRB_RATINGS = [
    ('Everyone', 'Everyone'),
    ('Everyone 10+', 'Everyone 10+'),
    ('Teen', 'Teen'),
    ('Mature 17+', 'Mature 17+'),
    ('Adults Only 18+', 'Adults Only 18+'),
    ('Rating Pending', 'Rating Pending'),
]

GENRES = [
    ('Action', 'Action'),
    ('Adventure', 'Adventure'),
    ('Arcade', 'Arcade'),
    ('Board', 'Board'),
    ('Card', 'Card'),
    ('Casual', 'Casual'),
    ('Educational', 'Educational'),
    ('Fighting', 'Fighting'),
    ('Indie', 'Indie'),
    ('MMO', 'MMO'),
    ('Open World', 'Open World'),
    ('Platformer', 'Platformer'),
    ('Racing', 'Racing'),
    ('RPG', 'RPG'),
    ('Shooter', 'Shooter'),
    ('Sim', 'Sim'),
    ('Sports', 'Sports'),
    ('Strategy', 'Strategy'),
]

class Game(models.Model):
    title = models.CharField(max_length=100, verbose_name='Game Title', db_column='game_title', blank=False, null=False, unique=True)
    publisher = models.CharField(max_length=50, verbose_name='Publisher', db_column='publisher', blank=True, null=True)
    ESRB_rating = models.CharField(max_length=20, verbose_name='ESRB Rating', db_column='ESRB', blank=True, null=True, choices=ESRB_RATINGS)
    genre = models.CharField(max_length=30, verbose_name='Genre', db_column='genre', blank=False, null=True, choices=GENRES)
    release_date = models.DateField(verbose_name='Release Date', db_column='release_date', blank=True, null=True)
    user_rating = models.IntegerField(verbose_name='User Rating', db_column='user_rating', choices=USER_RATINGS, blank=True, null=True)

    class Meta:
        db_table = 'games_tbl'
        verbose_name = 'Game'