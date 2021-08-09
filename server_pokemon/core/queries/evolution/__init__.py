from core.shared.actions.get import get_pokemon, convert_pokemon
from core.shared.domain.pokemon import Pokemon
from pokemon_base import models as db


def get_pokemon_evolutions(pokemon: Pokemon):
    return {
        '__typename': 'Evolution',
        'from': get_pokemon(pokemon.evolves_from.id) if pokemon.evolves_from else None,
        'to': [
            convert_pokemon(pokemon)
            for pokemon in db.Pokemon.objects.filter(evolves_from_id=pokemon.number)
        ],
        'gender': pokemon.evolves_from.gender if pokemon.evolves_from else None
    }
