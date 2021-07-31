from typing import Iterable

from core.shared.domain.pokemon import Pokemon
from core.shared.actions.save import save_pokemons

def update_pokemons(pokemons: Iterable[Pokemon]) -> None:
    save_pokemons(pokemons)