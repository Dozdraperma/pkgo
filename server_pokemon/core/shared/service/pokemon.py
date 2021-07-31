from abc import ABC, abstractmethod
from typing import List

from core.shared.domain.pokemon import Pokemon


class PokemonRepository(ABC):

    @abstractmethod
    def get_pokemons(self) -> List[Pokemon]:
        pass
