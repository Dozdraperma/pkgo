import json
import re
from pathlib import Path
from typing import Dict, Set, List, Tuple, Optional

from pokemon_base.exceptions import ParserError, ValidationError
from pokemon_base.models import Pokemon


def convert_to_snake_case(item: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', item).lower()


def convert_to_camel_case(item: str) -> str:
    special_case = {
        'max_cp': 'maxCP'
    }
    if item in special_case:
        return special_case[item]
    components = item.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


def get_pokemon_fields() -> List[str]:
    return [
        field
        for field in Pokemon._meta.get_fields()
        if field.name != 'pokemon'
    ]


def get_stage(raw_pok: Dict) -> int:
    if not raw_pok['evolution'].get('pastBranch'):
        return 0
    if not raw_pok['evolution']['pastBranch'].get('pastBranch'):
        return 1
    return 2


def validate_pokemon(pok: Dict) -> Set[Exception]:
    errors = set()
    required = {field.name for field in get_pokemon_fields() if not field.null and not field.blank}

    if unresolved := [field for field, value in pok.items() if value is None and field in required]:
        errors.add(ParserError(f'Unresolved field(s) in result: {", ".join(unresolved)}'))

    return errors


def find_infancy(pokemon: Pokemon, pokedex: List[Dict]) -> Optional[Tuple[str, str]]:
    gender = None
    # Find pokemon in pokedex
    try:
        pokemon_dex = list(filter(
            lambda pok: pok['name'] == pokemon.name,
            pokedex
        )).pop(0)
    except KeyError:
        raise ParserError(f'Unable to find {pokemon["name"]} in pokedex')

    if not pokemon_dex['evolution'].get('pastBranch'):
        return

    if 'Female' in pokemon_dex['family']['name']:
        gender = 'Female'
    if 'Male' in pokemon_dex['family']['name']:
        gender = 'Male'

    infancy_name = pokemon_dex['evolution']['pastBranch']['name'].replace('Male', '').replace('Female', '').strip()

    # Find infancy in pokedex
    try:
        infancies = list(filter(
            lambda pok: pok['name'] == infancy_name,
            pokedex
        ))
        if len(infancies) > 1:
            infancy = list(filter(
                lambda pok: gender in pok['family']['name'],
                infancies
            )).pop(0)
        else:
            infancy = infancies.pop(0)

    except KeyError:
        raise ParserError(f'Unable to find infancy for {pokemon["name"]}, search for - {infancy_name}')

    return infancy['dex'], gender


def parse_pokemon(raw: Dict) -> Pokemon:
    """
    Pokemon parser from json by rules below
    :param raw:
    :return:
    """

    # Append simple values
    pokemon = {
        'id': raw['dex'],
        'name': raw['name'],
        'height': int(raw['height'] * 100),
        'weight': int(raw['weight'] * 100),
        'max_cp': raw['maxCP'],
        'family_name': raw['family']['name'],
        'base_attack': raw['stats']['baseAttack'],
        'base_defense': raw['stats']['baseDefense'],
        'base_stamina': raw['stats']['baseStamina'],
        'primary_type': raw['types'][0]['name'],
        'secondary_type': raw['types'][1]['name'] if len(raw['types']) == 2 else '',
        'stage': get_stage(raw),
    }

    # Validation
    if errors := validate_pokemon(pokemon):
        raise ValidationError(f'Validate failed due to error(s): {", ".join({str(error) for error in errors})}')

    return Pokemon(**pokemon)


def resolve_evolutions(pokemons: List[Pokemon], pokedex: List[Dict]) -> List[Pokemon]:
    for pokemon in pokemons:
        infancy_dex, gender = find_infancy(pokemon, pokedex) or (None, None)

        if not infancy_dex:
            continue

        pokemon.evolves_from_id = infancy_dex
        pokemon.evolve_gender = gender

    return pokemons


def pokedex_parser(datapath: Path):
    with open(datapath, 'r') as pokedex:
        pokedex = json.loads(pokedex.read())

    pokemons = [parse_pokemon(pokemon) for pokemon in pokedex]
    pokemons = resolve_evolutions(pokemons, pokedex)

    # Assert we processed all pokemons from source
    assert len(pokedex) == len(pokemons), 'Number of pokemons not equal number of pokemons in pokedex'

    # Remove repeated pokemons (probably because unsupported cases)
    pokemons = set(pokemons)

    # Save pokemons to db
    Pokemon.objects.bulk_create(pokemons)
