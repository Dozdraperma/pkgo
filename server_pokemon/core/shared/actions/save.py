from typing import Iterable

import pokemon_base.models as db
from core.shared.domain.pokemon import Pokemon

__all__ = [
    'save_pokemons',
]


def _convert_to_db_object(pokemon: Pokemon) -> db.Pokemon:
    pokemon_db = db.Pokemon(**pokemon.dict(exclude={'evolves_from', }))
    pokemon_db.evolves_from_id = pokemon.evolves_from
    return pokemon_db


def save_pokemons(pokemons: Iterable[Pokemon]) -> None:
    db.Pokemon.objects.bulk_create([
        _convert_to_db_object(pokemon)
        for pokemon in pokemons
    ])
