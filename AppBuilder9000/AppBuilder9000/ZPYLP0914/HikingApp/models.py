from django.db import models


class create_happ_user(models.Model):
    # default manager (object) changed to admin
    admin = models.Manager()

    # fields = field types(field options)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    # primary key
    nick_name = models.CharField(primary_key=True, max_length=30, blank=False)
    street_address = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=False)
    country = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=30, blank=False)
    password = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.nick_name


# choices available for model hiking db hike_preferences
hike_type = [
    ('Flat', 'Flat'),
    ('Hilly', 'Hilly'),
    ('Mountains', 'Mountains'),
    ('Rivers', 'Rivers'),
    ('Glacier', 'Glacier'),
    ('Lake', 'Lake')
]

hike_length = [
    ('1-2 Miles', '1-2 Miles'),
    ('2-5 Miles,', '2-5 Miles'),
    ('5-8 Miles', '5-8 Miles'),
    ('8-10 Miles', '8-10 Miles'),
    ('10+ Miles', '10+ Miles')
]

healthy = [
    ('Not to Healthy', 'Not to Healthy'),
    ('Somewhat Healthy', 'Somewhat Healthy'),
    ('Healthy', 'Healthy'),
    ('Pretty Healthy', 'Pretty Healthy'),
    ('Very Healthy', 'Very Healthy')
]

avid = [
    (True, 'Yes'),
    (False, 'No')
]


class hike_preferences(models.Model):
    # default manager (object) changed to admin
    admin = models.Manager()

    # fields = field types(field options)
    # One To One Field relationship with Primary Key
    nick_name = models.OneToOneField(create_happ_user, on_delete=models.CASCADE)
    favorite_types_of_hikes = models.CharField(max_length=30, choices=hike_type, blank=False)
    perfect_length_of_hike = models.CharField(max_length=30, choices=hike_length, blank=False)
    avid_hiker = models.BooleanField(choices=avid, default=False)
    how_healthy_are_you = models.CharField(max_length=30, choices=healthy, blank=False)

    def __str__(self):
        return self.nick_name