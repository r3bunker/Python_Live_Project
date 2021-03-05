from django.db import models


GAME_GENRES = [
    ('RPG', 'RPG'),
    ('FPS', 'FPS'),
    ('MMO', 'MMO'),
    ('Adventure', 'Adventure'),
    ('Action', 'Action'),
    ('Simulation', 'Simulation'),
    ('Fighting', 'Fighting'),
    ('Text-Based', 'Text-Based'),
    ('Platformer', 'Platformer'),
    ('Survival', 'Survival'),
    ('Indie', 'Indie'),
    ('Card', 'Card'),
    ('Stealth', 'Stealth'),
    ('Rhythm/Dance', 'Rhythm/Dance'),
    ('Turn-Based', 'Turn-Based'),
    ('Strategy', 'Strategy'),
    ('Sports', 'Sports'),
]


class User(models.Model):
    first_name = models.CharField(max_length=30, blank=False, verbose_name="First Name")
    last_name = models.CharField(max_length=30, blank=False, verbose_name="Last Name")
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    username = models.CharField(max_length=50, blank=False, unique=True)
    email = models.EmailField(max_length=50, blank=False)
    fav_genre = models.CharField(max_length=50, choices=GAME_GENRES, default='', verbose_name="Favorite Game Genre?")

    Profiles = models.Manager()

    def __str__(self):
        return self.username


USER_RATING = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
]


class Game(models.Model):
    game_title = models.CharField(max_length=80, blank=False, null=False, unique=True, verbose_name="Game Title")
    game_genre = models.CharField(max_length=30, blank=True, null=True, choices=GAME_GENRES, verbose_name="Genre")
    game_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Price")
    game_publisher = models.CharField(max_length=30, blank=False, null=True, verbose_name="Publisher")
    game_user_rating = models.IntegerField(blank=True, null=True, choices=USER_RATING, verbose_name="User Rating")

    Games = models.Manager()

    def __str__(self):
        return self.game_title
