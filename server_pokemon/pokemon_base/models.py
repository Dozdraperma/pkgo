from django.db import models


class Pokemon(models.Model):
    def __str__(self):
        return self.name

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
        GHOST = 'GH', 'Ghost'
        DRAGON = 'DG', 'Dragon'
        STEEL = 'ST', 'Steel'
        DARK = 'DK', 'Dark'
        FAIRY = 'FA', 'Fairy'

    class InfancyGender(models.TextChoices):
        MALE = 'ML', 'Male'
        FEMALE = 'FL', 'Female'

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
    evolves_from = models.ForeignKey('self', on_delete=models.DO_NOTHING, related_name='evolves_to', null=True)
    evolve_gender = models.CharField(choices=InfancyGender.choices, null=True, max_length=50)
    description = models.TextField(max_length=500, blank=True)
