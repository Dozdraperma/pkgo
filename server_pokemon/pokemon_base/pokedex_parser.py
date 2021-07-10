import json
import re
from dataclasses import dataclass
from pprint import pprint
from typing import Dict, Generator

from django.conf import settings

from pokemon_base.exceptions import ParserError
from pokemon_base.models import Pokemon


@dataclass
class ParserResult:
    pokemon: Dict

    def calculate_unresolved(self) -> Generator:
        return (
            field
            for field in get_pokemon_fields()
            if field not in self.pokemon.keys()
        )


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
        field.name
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
        'secondary_type': raw_pok['types'][1]['name'] if len(raw_pok['types']) == 2 else None
    }


def parse_pokemon(raw_pok: Dict):
    """
    Pokemon parser from json by rules below
    :param pokemon:
    :return:
    """

    # Get values from first level of raw source
    result = {
        field: raw_pok.get(convert_to_camel_case(field))
        for field in get_pokemon_fields()
    }

    # Append base stats values
    result |= get_base_stats(raw_pok)

    # Append family name and types
    result['family_name'] = raw_pok['family']['name']
    result |= get_types(raw_pok)

    # Reassign evolution field
    result['evolution'] = [evolution['name'] for evolution in raw_pok['evolution']['futureBranches']]

    return result


def pokedex_parser():
    pokedex_path = settings.BASE_DIR / 'pokedex.json'

    with open(pokedex_path, 'r') as pokedex:
        pokedex = json.loads(pokedex.read())
    result = parse_pokemon(pokedex[0])
    if unresolved := [field for field, value in result.items() if value is None]:
        raise ParserError(f'Unresolved field(s) in result - {", ".join(unresolved)}')
    pprint(result)
