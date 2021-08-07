from typing import Iterable

import pokemon_base.models as db
from core.shared.domain.pokemon import Pokemon

__all__ = [
    'save_pokemon',
]


def _convert_to_db_object(pokemon: Pokemon) -> db.Pokemon:
    pokemon_db = db.Pokemon(
        id=pokemon.number,
        name=pokemon.name,
        height=pokemon.height * 1000,
        weight=pokemon.weight * 1000,
        max_cp=pokemon.max_cp,
        family_name=pokemon.family_name,
        base_attack=pokemon.base_attack,
        base_defense=pokemon.base_defense,
        base_stamina=pokemon.base_stamina,
        primary_type=pokemon.primary_type.value,
        secondary_type=pokemon.secondary_type.value if pokemon.secondary_type else '',
        evolves_from_id=pokemon.evolves_from.id if pokemon.evolves_from else None,
        evolve_gender=pokemon.evolves_from.gender if pokemon.evolves_from else None,
        description=pokemon.description
    )
    return pokemon_db


def save_pokemons(pokemons: Iterable[Pokemon]) -> None:
    db.Pokemon.objects.bulk_create([
        _convert_to_db_object(pokemon)
        for pokemon in pokemons
    ])


def save_pokemon(pokemon: Pokemon) -> None:
    _convert_to_db_object(pokemon).save()
