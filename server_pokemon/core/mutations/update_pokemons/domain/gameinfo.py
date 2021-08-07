from typing import Optional, List

from pydantic import BaseModel, conint

from core.shared.domain.pokemon import Type, Stage, Gender


class PokemonBaseInfo(BaseModel):
    number: conint(gt=0)
    generation: conint(gt=0)
    name: str
    max_cp: conint(gt=0)
    primary_type: Type
    secondary_type: Optional[Type]
    family_name: str


class GenerationItem(BaseModel):
    id: conint(gt=0)
    name: str
    required_gender: Optional[Gender]


class Generation(BaseModel):
    stage: Stage
    pokemons: Optional[List[GenerationItem]]
