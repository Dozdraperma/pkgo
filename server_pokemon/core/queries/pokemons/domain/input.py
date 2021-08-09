from enum import Enum
from typing import Optional

from pydantic import BaseModel, constr, conint

from core.shared.domain.pokemon import Type


class StatsFiltrationMode(Enum):
    EQUALS = 'exact'
    LESS_THAN = 'lt'
    GREATER_THAN = 'gt'


class StatsInput(BaseModel):
    max_cp: Optional[conint(gt=0, lt=5000)]
    base_attack: Optional[conint(gt=0, lt=500)]
    base_defense: Optional[conint(gt=0, lt=500)]
    base_stamina: Optional[conint(gt=0, lt=500)]
    mode: StatsFiltrationMode

    class Config:
        frozen = True


class FilterInput(BaseModel):
    name: Optional[
        constr(
            strip_whitespace=True,
            to_lower=True,
            min_length=3,
            max_length=30,
        )
    ]
    type: Optional[Type]
    stats: Optional[StatsInput]

    class Config:
        frozen = True


class SearchInput(BaseModel):
    name: constr(
        strip_whitespace=True,
        to_lower=True,
        min_length=3,
        max_length=30,
    )
    include_evolutions: bool

    class Config:
        frozen = True
