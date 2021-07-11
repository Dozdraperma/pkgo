import json
import re
from pathlib import Path
from typing import Dict, Set, List, Tuple, Iterable, Optional

from pokemon_base.exceptions import ParserError, ValidationError
from pokemon_base.models import Pokemon, AbstractPokemon


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


def get_pokemon_fields():
    return [
        field
        for field in Pokemon._meta.get_fields()
        if field.name != 'pokemon'
    ]


def get_base_stats(raw_pok: Dict) -> Dict:
    return {
        convert_to_snake_case(stat): value
        for stat, value in raw_pok['stats'].items()
    }


def get_types(raw_pok: Dict) -> Dict:
    return {
        'primary_type': raw_pok['types'][0]['name'],
        'secondary_type': raw_pok['types'][1]['name'] if len(raw_pok['types']) == 2 else ''
    }


def get_stage(raw_pok: Dict) -> int:
    if not raw_pok['evolution'].get('pastBranch'):
        return 0
    if not raw_pok['evolution']['pastBranch'].get('pastBranch'):
        return 1
    return 2


def get_infancy(raw_pok: Dict) -> str:
    past_branch = raw_pok['evolution'].get('pastBranch')
    if past_branch:
        return past_branch['name']


def validate_pokemon(pok: Dict) -> Set[Exception]:
    errors = set()
    required = {field.name for field in get_pokemon_fields() if not field.null and not field.blank}

    if unresolved := [field for field, value in pok.items() if value is None and field in required]:
        errors.add(ParserError(f'Unresolved field(s) in result: {", ".join(unresolved)}'))

    return errors


def find_infancy(pokemon: Dict, pokemons: Iterable[AbstractPokemon]) -> Tuple[AbstractPokemon, Optional[str]]:
    gender = None

    if 'Female' in pokemon['infancy']:
        gender = 'Female'
    if 'Male' in pokemon['infancy']:
        gender = 'Male'

    infancy = pokemon['infancy'].replace('Male', '').replace('Female', '').strip()

    try:
        return set(filter(lambda x: x.name == infancy, pokemons)).pop(), gender
    except KeyError:
        raise ParserError(f'Unable to find infancy for {pokemon["name"]}')


def find_regional(raw_pok: Dict) -> Optional[str]:
    forms = ['Alola', 'Galar']
    for form in forms:
        return form if form in raw_pok['name'] else None


def find_firn(raw_pok: Dict) -> Optional[List[str]]:
    forms = raw_pok.pop('forms')
    if not forms:
        return


def parse_pokemon(raw_pok: Dict) -> Dict:
    """
    Pokemon parser from json by rules below
    :param raw_pok:
    :return:
    """

    # Get values from first level of raw source
    result = {
        field.name: raw_pok.get(convert_to_camel_case(field.name))
        for field in get_pokemon_fields()
    }

    # Append base stats values
    result |= get_base_stats(raw_pok)

    # Append family name and types
    result['family_name'] = raw_pok['family']['name']
    result |= get_types(raw_pok)

    # Append stage
    result['stage'] = get_stage(raw_pok)

    # Append regional form if exists
    # result['regional_variant'] = find_regional(raw_pok)
    result['regional_variant'] = None

    # Reassign fields
    result['infancy'] = get_infancy(raw_pok)
    result['id'] = raw_pok['dex']

    # Metrics enhancements
    result['height'] = int(result['height'] * 100)
    result['weight'] = int(result['weight'] * 100)

    # Validation
    if errors := validate_pokemon(result):
        raise ValidationError(f'Validate failed due to error(s): {", ".join({str(error) for error in errors})}')

    return result


def pokemons_processor(poks: List[Dict]) -> List[Pokemon]:
    """
    TODO: Handle forms of pokemon
    TODO: Handle region of pokemon
    Create list of ORM objects from raw-dict
    :param poks:
    :return:
    """
    pokemons = [
        Pokemon(**pok)
        for pok in poks
        if pok['stage'] == 0
    ]

    for pok in [pok for pok in poks if pok['stage'] == 1]:
        pok['infancy'], pok['infancy_gender'] = find_infancy(pok, pokemons)
        pokemons.append(Pokemon(**pok))

    for pok in [pok for pok in poks if pok['stage'] == 2]:
        pok['infancy'], pok['infancy_gender'] = find_infancy(pok, pokemons)
        pokemons.append(Pokemon(**pok))

    return pokemons


def pokedex_parser(datapath: Path):
    with open(datapath, 'r') as pokedex:
        pokedex = json.loads(pokedex.read())

    raw_pokemons = [parse_pokemon(pokemon) for pokemon in pokedex]
    pokemons = pokemons_processor(raw_pokemons)

    # Assert we processed all pokemons from source
    assert len(pokedex) == len(pokemons), 'Number of pokemons not equal number of pokemons in pokedex'

    # Remove repeated pokemons (probably because unsupported cases)
    pokemons = set(pokemons)

    # Save pokemons to db
    Pokemon.objects.bulk_create(pokemons)
