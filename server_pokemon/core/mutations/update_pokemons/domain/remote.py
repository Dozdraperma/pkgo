import enum
from typing import Optional

from pydantic import BaseModel, conint

from core.shared.domain.pokemon import Type


class PokemonBaseInfo(BaseModel):
    number: conint(gt=0)
    generation: conint(gt=0)
    name: str
    max_cp: conint(gt=0)
    primary_type: Type
    secondary_type: Optional[Type]
    family_name: str
