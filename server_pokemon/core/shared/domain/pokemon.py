from enum import Enum
from typing import Optional

from pydantic import BaseModel, conint, confloat


class Type(Enum):
    NORMAL = 'Normal'
    FIRE = 'Fire'
    WATER = 'Water'
    GRASS = 'Grass'
    ELECTRIC = 'Electric'
    ICE = 'Ice'
    FIGHTING = 'Fighting'
    POISON = 'Poison'
    GROUND = 'Ground'
    FLYING = 'Flying'
    PSYCHIC = 'Psychic'
    BUG = 'Bug'
    ROCK = 'Rock'
    GHOST = 'Ghost'
    DRAGON = 'Dragon'
    STEEL = 'Steel'
    DARK = 'Dark'
    FAIRY = 'Fairy'


class Stage(Enum):
    UNEVOLVED = 0
    FIRST = 1
    SECOND = 2


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'


class Evolution(BaseModel):
    id: conint(gt=0)
    name: str
    gender: Optional[Gender]


class Pokemon(BaseModel):
    number: conint(gt=0, lt=1000)
    name: str
    height: confloat(gt=0)
    weight: confloat(gt=0)
    max_cp: conint(gt=0)
    base_attack: conint(gt=0)
    base_defense: conint(gt=0)
    base_stamina: conint(gt=0)
    primary_type: Type
    secondary_type: Optional[Type]
    evolves_from: Optional[Evolution]
    family_name: str
    description: Optional[str]


class PokemonBaseInfo(BaseModel):
    number: conint(gt=0)
    name: str
