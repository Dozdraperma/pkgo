import json
import sys
from collections import defaultdict

from pydantic import ValidationError

import pokemon_base.models as db
from core.mutations.update_pokemons.domain.gameinfo import PokemonBaseInfo
from core.mutations.update_pokemons.services.gameinfo import PokemonGameinfo
from core.shared.actions.get import get_pokemon
from core.shared.actions.save import save_pokemon
from core.shared.domain.pokemon import Evolution, Pokemon
from core.shared.service.log import logger
from core.shared.service.pokemon import PokemonRepository
from server_pokemon import settings

EXCLUDED = [
    'Zacian',
    'Zamazenta',
    'Urshifu',
    'Calyrex'
]

VALIDATION_RESULT_PATH = settings.BASE_DIR / 'logs'
VALIDATION_RESULT_PATH.mkdir(parents=True, exist_ok=True)


def _pokemon_in_db(number: int) -> bool:
    return bool(db.Pokemon.objects.filter(pk=number))


def update_evolution(pokemon: Pokemon, evolution: Evolution) -> None:
    db.Pokemon.objects.filter(pk=pokemon.number).update(
        evolves_from_id=evolution.id,
        evolve_gender=evolution.gender
    )


def update_pokemons(
        repository: PokemonRepository,
) -> None:
    pokemons = repository.get_pokemon_list()
    validation_failed = defaultdict(list)
    with open(VALIDATION_RESULT_PATH / 'updating.json', 'r') as log:
        validation_cache = json.load(log)
        validation_cache = {
            pokemon[1]
            for pokemons in validation_cache.values()
            for pokemon in pokemons
        }

    for pokemon in pokemons:
        sys.stdout.write(f'Processing {pokemon.name}... ')
        if pokemon.name in EXCLUDED:
            sys.stdout.write('EXCLUDED\n')
            continue
        if pokemon.name in validation_cache:
            sys.stdout.write('INVALID (cached)\n')
            continue
        if _pokemon_in_db(pokemon.number):
            sys.stdout.write('PASS\n')
            continue
        try:
            save_pokemon(
                pokemon=repository.get_pokemon(pokemon.number)
            )
            sys.stdout.write('SAVED\n')
        except ValidationError as err:
            sys.stdout.write('INVALID\n')
            for error in err.errors():
                validation_failed[error['loc'][0]].append((pokemon.number, pokemon.name))

    if not validation_cache:
        with open(VALIDATION_RESULT_PATH / 'updating.json', 'w+') as log:
            json.dump(validation_failed, log)

    for pokemon in pokemons:
        logger.info(f'Update evolution for {pokemon.name}...')
        evolution = repository.get_evolution(pokemon.name)
        if evolution is None:
            continue
        update_evolution(
            pokemon=get_pokemon(pokemon.number),
            evolution=evolution
        )
