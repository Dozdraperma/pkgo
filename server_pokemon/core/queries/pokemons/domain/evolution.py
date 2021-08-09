from typing import List

from pydantic import BaseModel, conint

from core.shared.domain.pokemon import Pokemon


class EvolutionStage(BaseModel):
    stage_count: conint(gt=0)
    pokemons: List[Pokemon]

    class Config:
        frozen = True


class Branch(BaseModel):
    stages: List[EvolutionStage]

    class Config:
        frozen = True
