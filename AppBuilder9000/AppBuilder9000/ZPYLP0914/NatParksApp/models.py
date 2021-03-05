# from django.db import models
#
# # Create your models here.
#
# # Let's you choose which national park to leave a review on
# natParks_choices = [
#     ('Arches National Park', 'Arches National Park'),
#     ('Bryce National Park', 'Bryce National Park'),
#     ('Glacier National Park', 'Glacier National Park'),
#     ('Grand Canyon National Park', 'Grand Canyon National Park'),
#     ('Grand Teton National Park', 'Grand Teton National Park'),
#     ('Haleakala National Park', 'Haleakala National Park'),
#     ('Rocky Mountains National Park', 'Rocky Mountains National Park'),
#     ('Yellowstone National Park', 'Yellowstone National Park'),
#     ('Yosemite National Park', 'Yosemite National Park'),
#     ('Zion National Park', 'Zion National Park'),
# ]
#
#
# # fields for form on .html page
#
# class natParksReview(models.Model):
#     pk = id
#     park_name = models.CharField(max_length=350, choices=natParks_choices)
#     date_arrived = models.DateField()
#     date_departed = models.DateField()
#     review_park = models.TextField()
#
#     objects = models.Manager()
#
#     # return national park name
#
#     def __str__(self):
#         return self.park_name
#
#
# class NewsletterUser(models.Model):
#     email = models.EmailField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.email
