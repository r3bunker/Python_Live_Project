from django.db import models

YES_OR_NO = [
    (True, 'Yes'),
    (False, 'No'),
]

class Contact(models.Model):
    first_Name = models.CharField(max_length=50, default='', blank=False, null=False)
    last_Name = models.CharField(max_length=50, default='', blank=False, null=False)
    email_Address = models.EmailField(max_length=50, blank=False, null=False)
    covid_Question = models.BooleanField(verbose_name='Have you been affected by Covid?', choices=YES_OR_NO, default='Yes')
    story_Questions = models.TextField(verbose_name="Tell us your Silver Lining Story", max_length=1000, default='', blank=False, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.first_Name

