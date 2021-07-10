from django.db import models


class Pokemon(models.Model):

    class Type(models.TextChoices):
        NORMAL = 'NR', 'Normal'
        FIRE = 'FR', 'Fire'
        WATER = 'WT', 'Water'
        GRASS = 'GS', 'Grass'
        ELECTRIC = 'EL', 'Electric'
        ICE = 'IC', 'Ice'
        FIGHTING = 'FT', 'Fighting'
        POISON = 'PO', 'Poison'
        GROUND = 'GD', 'Ground'
        FLYING = 'FL', 'Flying'
        PSYCHIC = 'PY', 'Psychic'
        BUG = 'BG', 'Bug'
        ROCK = 'RK', 'Rock'
        GHOST = 'DK', 'Dark'
        DRAGON = 'DG', 'Dragon'
        STEEL = 'ST', 'Steel'
        FAIRY = 'FA', 'Fairy'

    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    height = models.SmallIntegerField(editable=True)
    weight = models.SmallIntegerField(editable=True)
    max_cp = models.PositiveSmallIntegerField()
    family_name = models.CharField(max_length=100)
    base_attack = models.PositiveSmallIntegerField()
    base_defense = models.PositiveSmallIntegerField()
    base_stamina = models.PositiveSmallIntegerField()
    primary_type = models.CharField(choices=Type.choices, default=Type.NORMAL, max_length=100)
    secondary_type = models.CharField(choices=Type.choices, blank=True, max_length=100)
    infancy = models.OneToOneField('self', on_delete=models.SET_NULL, null=True)

