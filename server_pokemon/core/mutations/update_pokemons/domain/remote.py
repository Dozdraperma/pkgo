import enum
from typing import Optional

from pydantic import BaseModel, conint


class Type(enum.Enum):
    NORMAL = 1
    FIGHTING = 2
    FLYING = 3
    POISON = 4
    GROUND = 5
    ROCK = 6
    BUG = 7
    GHOST = 8
    STEEL = 9
    FIRE = 10
    WATER = 11
    GRASS = 12
    ELECTRIC = 13
    PSYCHIC = 14
    ICE = 15
    DRAGON = 16
    DARK = 17
    FAIRY = 18


class PokemonBaseInfo(BaseModel):
    number: conint(gt=0)
    generation: conint(gt=0)
    name: str
    max_cp: conint(gt=0)
    primary_type: Type
    secondary_type: Optional[Type]
