from django.db import models


class AbstractPokemon(models.Model):
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

    class Stage(models.IntegerChoices):
        UNEVOLVED = 0
        FIRST = 1
        SECOND = 2

    class InfancyGender(models.TextChoices):
        MALE = 'ML', 'Male'
        FEMALE = 'FL', 'Female'

    class Meta:
        abstract = True

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
    stage = models.PositiveSmallIntegerField(Stage.choices, default=Stage.UNEVOLVED)
    infancy_gender = models.CharField(choices=InfancyGender.choices, null=True, max_length=50)


class Pokemon(AbstractPokemon):
    regional_variant = models.OneToOneField('RegionalPokemon', on_delete=models.CASCADE, null=True, related_name='+')
    infancy = models.ForeignKey('Pokemon', on_delete=models.SET_NULL, null=True)


class RegionalPokemon(AbstractPokemon):
    class Variant(models.TextChoices):
        ALOLA = 'AL', 'Alola'
        GALAR = 'GL', 'Galar'

    variant = models.CharField(choices=Variant.choices, max_length=50)
    infancy = models.OneToOneField('RegionalPokemon', on_delete=models.SET_NULL, null=True)


class FormPokemon(AbstractPokemon):
    pass

