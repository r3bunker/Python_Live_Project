from django.db import models

# Create your models here.



class Star(models.Model):
    star_name = models.CharField(verbose_name="Star Name", max_length=50);
    star_type = models.CharField(verbose_name="Type", max_length=50);
    atmosphere = models.CharField(verbose_name="Atmosphere", max_length=50);
    star_temp = models.IntegerField(verbose_name="Star Temperature", default="", blank=True, null=True);
    star_distance = models.IntegerField(verbose_name="Distance from Earth", default="", blank=True, null=True);
    star_mass = models.IntegerField(verbose_name="Mass", default="", blank=True, null=True);
    image = models.CharField(max_length=255, default='', blank=True);


    stars = models.Manager()

    def __str__(self):
        return self.star_name



class Planet(models.Model):

    planet_name = models.CharField(verbose_name="Planet", max_length=50);
    planet_diameter = models.IntegerField(verbose_name="Diameter", default="", blank=True, null=True);
    planet_mass = models.IntegerField(verbose_name="Mass", default="", blank=True, null=True);
    planet_area = models.IntegerField(verbose_name="Area", default="", blank=True, null=True);
    sun_distance = models.IntegerField(verbose_name="Distance from the Sun", default="", blank=True, null=True);
    planet_orbit = models.IntegerField(verbose_name="Orbit Time", default="", blank=True, null=True);
    gravity = models.FloatField(verbose_name="Gravity", default="0.00", blank=True, null=True);
    image = models.CharField(max_length=255, default='', blank=True);

    planets = models.Manager()

    def __str__(self):
        return self.planet_name



class Moon(models.Model):
    moon_name = models.CharField(verbose_name="Name", max_length=50);
    moon_planet = models.CharField(verbose_name="Planet", max_length=50);
    moon_diameter = models.IntegerField(verbose_name="Diameter", default="", blank=True, null=True);
    moon_phase = models.CharField(verbose_name="Phase", max_length=50);
    moon_phaseDeg = models.IntegerField(verbose_name="Phase Degree", default="", blank=True, null=True);
    moon_orbit = models.IntegerField(verbose_name="Orbit Time", default="", blank=True, null=True);
    image = models.CharField(max_length=255, default='', blank=True);

    moons = models.Manager()

    def __str__(self):
        return self.moon_name