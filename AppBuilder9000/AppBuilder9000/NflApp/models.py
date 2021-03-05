from django.db import models

# provides position choices
POSITION_CHOICES = [
    ('QB', 'QB'),
    ('WR', 'WR'),
    ('RB', 'RB'),
    ('TE', 'TE'),
    ('OL', 'OL'),
    ('DL', 'DL'),
    ('LB', 'LB'),
    ('DB', 'DB'),
]

TEAM_CHOICES = [
    ('Arizona Cardinals','Arizona Cardinals'),
    ('Atlanta Falcons','Atlanta Falcons'),
    ('Baltimore Ravens','Baltimore Ravens'),
    ('Buffalo Bills','Buffalo Bills'),
    ('Carolina Panthers','Carolina Panthers'),
    ('Chicago Bears','Chicago Bears'),
    ('Cincinnati Bengals','Cincinnati Bengals'),
    ('Cleveland Browns','Cleveland Browns'),
    ('Dallas Cowboys','Dallas Cowboys'),
    ('Denver Broncos','Denver Broncos'),
    ('Detroit Lions','Detroit Lions'),
    ('Green Bay Packers','Green Bay Packers'),
    ('Houston Texans','Houston Texans'),
    ('Indianapolis Colts','Indianapolis Colts'),
    ('Jacksonville Jaguars','Jacksonville Jaguars'),
    ('Kansas City Chiefs','Kansas City Chiefs'),
    ('Las Vegas Raiders','Las Vegas Raiders'),
    ('Los Angeles Chargers','Los Angeles Chargers'),
    ('Los Angeles Rams','Los Angeles Rams'),
    ('Miami Dolphins','Miami Dolphins'),
    ('Minnesota Vikings','Minnesota Vikings'),
    ('New England Patriots','New England Patriots'),
    ('New Orleans Saints','New Orleans Saints'),
    ('New York Giants','New York Giants'),
    ('New York Jets','New York Jets'),
    ('Philadelphia Eagles','Philadelphia Eagles'),
    ('Pittsburgh Steelers','Pittsburgh Steelers'),
    ('San Francisco 49ers','San Francisco 49ers'),
    ('Seattle Seahawks','Seattle Seahawks'),
    ('Tampa Bay Buccaneers','Tampa Bay Buccaneers'),
    ('Tennessee Titans','Tennessee Titans'),
    ('Washington Football Team','Washington Football Team'),
]

class PlayerProfile(models.Model):
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    name = models.CharField(max_length=60, default='')
    height = models.PositiveIntegerField(verbose_name='Height (Inches)')
    weight = models.PositiveIntegerField(verbose_name='Weight (Pounds)')
    team = models.CharField(max_length=30, choices=TEAM_CHOICES)

    objects = models.Manager()

    def __str__(self):
        return self.name
