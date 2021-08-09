from typing import Dict

from core.queries.pokemons.domain.input import FilterInput, StatsInput, StatsFiltrationMode, SearchInput
from core.shared.domain.pokemon import Type


def convert_filter_input(filter_input: Dict) -> FilterInput:
    return FilterInput(
        name=filter_input.get('name'),
        type=filter_input.get('type') and Type(filter_input.get('type')),
        stats=StatsInput(
            max_cp=filter_input['stats'].get('maxCP'),
            base_attack=filter_input['stats'].get('baseAttack'),
            base_defense=filter_input['stats'].get('baseDefense'),
            base_stamina=filter_input['stats'].get('baseStamina'),
            mode=StatsFiltrationMode(filter_input['stats']['mode']),
        ) if filter_input.get('stats') else None
    )


def convert_search_input(search_input: Dict) -> SearchInput:
    return SearchInput(
        name=search_input.get('name'),
        include_evolutions=search_input.get('includeEvolutions')
    )
