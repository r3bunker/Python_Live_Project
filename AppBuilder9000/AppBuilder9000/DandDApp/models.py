from django.db import models

Race_Choice = [
    ('Elf', 'Elf'),
    ('Half-Elf', 'Half-Elf'),
    ('Human', 'Human'),
    ('Half-orc', 'Half-orc'),
    ('Halfling', 'Halfling'),
    ('Dwarf', 'Dwarf'),
]

Character_Class_Choice = [
    ('Fighter', 'Fighter'),
    ('Wizard', 'Wizard'),
    ('Rouge', 'Rouge'),
    ('Ranger', 'Ranger'),
    ('Paladin', 'Paladin'),
    ('Druid', 'Druid'),
]


class CreateCharacter(models.Model):
    name = models.CharField(max_length=50, verbose_name='Your Characters Name', default='', null=False)
    race = models.CharField(max_length=50, choices=Race_Choice, null=False)
    character_class = models.CharField(max_length=50, choices=Character_Class_Choice, null=False)
    strength = models.IntegerField(null=False)
    dexterity = models.IntegerField(null=False)
    constitution = models.IntegerField(null=False)
    intelligence = models.IntegerField(null=False)
    wisdom = models.IntegerField(null=False)
    charisma = models.IntegerField(null=False)

    object = models.Manager()

    def __str__(self):
        return self.name
