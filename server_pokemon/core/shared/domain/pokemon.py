from enum import Enum
from typing import Optional

from pydantic import BaseModel, conint

class Type(Enum):
    NORMAL = ('Normal', )
    FIRE = ('Fire', )
    WATER = ('Water', )
    GRASS = ('Grass', )
    ELECTRIC = ('Electric', )
    ICE = ('Ice', )
    FIGHTING = ('Fighting', )
    POISON = ('Poison', )
    GROUND = ('Ground', )
    FLYING = ('Flying', )
    PSYCHIC = ('Psychic', )
    BUG = ('Bug', )
    ROCK = ('Rock', )
    GHOST = ('Ghost', )
    DRAGON = ('Dragon', )
    STEEL = ('Steel', )
    DARK = ('Dark', )
    FAIRY = ('Fairy', )

    def __init__(self, title):
        self.title = title

class Stage(Enum):
    UNEVOLVED = 0
    FIRST = 1
    SECOND = 2

class Gender(Enum):
    MALE = 0
    FEMALE = 1

class Pokemon(BaseModel):
    number: conint(gt=0, lt=1000)
    name: str
    height: conint(gt=0)
    weight: conint(gt=0)
    max_cp: conint(gt=0)
    base_attack: conint(gt=0)
    base_defense: conint(gt=0)
    base_stamina: conint(gt=0)
    primary_type: Type
    secondary_type: Optional[Type]
    stage: Stage
    evolves_from: conint(gt=0)
    evolve_gender: Gender

