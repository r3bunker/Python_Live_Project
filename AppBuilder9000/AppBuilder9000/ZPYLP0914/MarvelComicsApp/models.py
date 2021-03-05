from django.db import models

PREFERENCE = [
    ('Yes', 'Yes'),
    ('No', 'No'),
]

TEAMS = [
    ('The Avengers', 'The Avengers'),
    ('The X-Men', 'The X-Men'),
    ('Inhumans', 'Inhumans'),
    ('Fantastic 4', 'Fantastic 4'),
    ('Guardians of the Galaxy', 'Guardians of the Galaxy'),
    ('Other', 'Other'),
]

class Subscriber(models.Model):
    sub_username = models.CharField(verbose_name='Username', max_length=50, default="", unique=True, blank=False, null=False)
    sub_email = models.EmailField(verbose_name='Email', max_length=50, blank=False, null=False)
    sub_fname = models.CharField(verbose_name='First Name', max_length=50, blank=False, null=False)
    sub_lname = models.CharField(verbose_name='Last Name', max_length=50, blank=False, null=False)
    sub_dob = models.DateField(verbose_name='Date of Birth', max_length=20)
    sub_team = models.CharField(verbose_name='What is your favorite super team?', max_length=50, choices=TEAMS, default='')
    sub_preference = models.CharField(verbose_name='Do you prefer to read comics online?', max_length=5, choices=PREFERENCE, default='')


    object = models.Manager()

    def __str__(self):
        return self.sub_username




