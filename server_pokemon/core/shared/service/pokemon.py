from abc import ABC, abstractmethod
from typing import List, Iterable

from core.shared.domain.pokemon import Pokemon, PokemonBaseInfo, Evolution


class PokemonRepository(ABC):

    @abstractmethod
    def get_pokemon(self, *args, **kwargs) -> Pokemon:
        pass

    @abstractmethod
    def get_pokemon_list(self) -> List[PokemonBaseInfo]:
        pass

    @abstractmethod
    def get_evolution(self, name) -> Evolution:
        pass

    @abstractmethod
    def get_pokemons(self) -> Iterable[Pokemon]:
        pass
