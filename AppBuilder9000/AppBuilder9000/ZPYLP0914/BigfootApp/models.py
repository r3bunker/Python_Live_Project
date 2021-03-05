from django.db import models

COUNTRY_CHOICES = [
    ('Canada', 'Canada'),
    ('United States', 'United States')
]

STATE_CHOICES = [
    ('Alberta', 'AB'),
    ('Alaska', 'AK'),
    ('Alabama', 'AL'),
    ('Arkansas', 'AR'),
    ('Arizona', 'AZ'),
    ('British Columbia', 'BC'),
    ('California', 'CA'),
    ('Colorado', 'CO'),
    ('Connecticut', 'CT'),
    ('Washington DC', 'DC'),
    ('Delaware', 'DE'),
    ('Florida', 'FL'),
    ('Georgia', 'GA'),
    ('Hawaii', 'HI'),
    ('Iowa', 'IA'),
    ('Idaho', 'ID'),
    ('Illinois', 'IL'),
    ('Indiana', 'IN'),
    ('Kansas', 'KS'),
    ('Kentucky', 'KY'),
    ('Louisiana', 'LA'),
    ('Massachusetts', 'MA'),
    ('Manitoba', 'MB'),
    ('Maryland', 'MD'),
    ('Maine', 'ME'),
    ('Michigan', 'MI'),
    ('Minnesota', 'MN'),
    ('Missouri', 'MO'),
    ('Mississippi', 'MS'),
    ('Montana', 'MT'),
    ('New Brunswick', 'NB'),
    ('North Carolina', 'NC'),
    ('North Dakota', 'ND'),
    ('Nebraska', 'NE'),
    ('New Hampshire', 'NH'),
    ('New Jersey', 'NJ'),
    ('Newfoundland', 'NL'),
    ('New Mexico', 'NM'),
    ('Nova Scotia', 'NS'),
    ('Northwest Territories', 'NT'),
    ('Nunavut', 'NU'),
    ('Nevada', 'NV'),
    ('New York', 'NY'),
    ('Ohio', 'OH'),
    ('Oklahoma', 'OK'),
    ('Ontario', 'ON'),
    ('Oregon', 'OR'),
    ('Pennsylvania', 'PA'),
    ('Prince Edward Island', 'PE'),
    ('Quebec', 'QC'),
    ('Rhode Island', 'RI'),
    ('South Carolina', 'SC'),
    ('South Dakota', 'SD'),
    ('Saskatchewan', 'SK'),
    ('Tennessee', 'TN'),
    ('Texas', 'TX'),
    ('Utah', 'UT'),
    ('Vermont', 'VT'),
    ('Washington', 'WA'),
    ('Wisconsin', 'WI'),
    ('West Virgina', 'WV'),
    ('Wyoming', 'WY'),
    ('Yukon', 'YT'),
]


class Encounter(models.Model):
    username = models.CharField(max_length=60, default="", blank=False, null=False, unique=False)
    street = models.CharField(max_length=180, default="", verbose_name="Nearest Street Address", blank=False,
                              null=False)
    city = models.CharField(max_length=100, default="", verbose_name="Nearest City", blank=False, null=False)
    state = models.CharField(max_length=80, verbose_name="State or Province", choices=STATE_CHOICES, blank=False, null=False)
    postal_code = models.CharField(max_length=10, default="", verbose_name="Postal Code", blank=False, null=False)
    country = models.CharField(max_length=60, choices=COUNTRY_CHOICES, null=False)
    enc_date = models.DateField(max_length=20, verbose_name="Encounter Date", blank=False, null=False)
    description = models.TextField(max_length=600, verbose_name="Brief Description Of Encounter", blank=True,
                                   null=False)
    enc_visual = models.BooleanField(verbose_name="Was This A Visual Encounter?", default=False)

    objects = models.Manager()

    def __str__(self):
        return self.username
