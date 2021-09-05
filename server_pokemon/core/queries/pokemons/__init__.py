import operator
from functools import reduce
from typing import List, Dict

from django.db.models import Q

import pokemon_base.models as db
from core.queries.pokemons.actions import convert_filter_input, convert_search_input
from core.queries.pokemons.domain.evolution import Branch, EvolutionStage
from core.queries.pokemons.domain.input import FilterInput, SearchInput
from core.shared.actions.get import convert_pokemon
from core.shared.domain.pokemon import Pokemon


# ToDo: type filtration

def get_filtration(filter_input: FilterInput) -> Q:
    filters = []
    if filter_input.name:
        filters.append(Q(name__icontains=filter_input.name))
    if filter_input.type:
        filters.append(
            Q(primary_type__iexact=filter_input.type.name)
            | Q(secondary_type__iexact=filter_input.type.name)
        )

    return reduce(operator.and_, filters)


def get_search(search_input: SearchInput) -> Q:
    return Q(name__icontains=search_input.name)


def get_pokemons(
        sort_input: List[str],
        filter_input: Dict,
        search_input: Dict,
        pagination_input: Dict,
) -> List[Pokemon]:
    query = db.Pokemon.objects.all()
    if filter_input is not None:
        filter_input = convert_filter_input(filter_input)
        query = query.filter(get_filtration(filter_input))

    if search_input is not None:
        search_input = convert_search_input(search_input)
        query = query.filter(get_search(search_input))

    if sort_input is not None:
        query = query.order_by(*sort_input)

    if pagination_input is not None:
        query = query[pagination_input['offset']:pagination_input['offset'] + pagination_input['limit']]

    return [
        convert_pokemon(pokemon)
        for pokemon in query
    ]


def get_evolution_branch(pokemon: Pokemon) -> Branch:
    query = db.Pokemon.objects.get(pk=pokemon.number)
    parent = query
    branch = []
    while True:
        if parent.evolves_from:
            parent = parent.evolves_from
        else:
            break

    parents = parent.evolves_to
    while parents:
        branch.append([
            parent for parent in parents.evolves_to
        ])
        parents = parent.evolves_to

    return Branch(
        stages=[
            EvolutionStage(
                pokemons=[
                    convert_pokemon(pokemon)
                    for pokemon in stage
                ],
                stage_count=i
            )
            for i, stage in enumerate(branch)
        ]
    )
