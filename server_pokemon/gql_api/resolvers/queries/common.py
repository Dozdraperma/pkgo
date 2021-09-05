from ariadne import convert_kwargs_to_snake_case

import gql_api.gql_api_types as gqt
from core.queries.pokemons import get_pokemons
from core.shared.actions.get import get_pokemon


@gqt.query.field('hello')
def resolve_hello(*_):
    return 'Hello from pokedex!'


@gqt.query.field('getPokemon')
@convert_kwargs_to_snake_case
def resolve_pokemon(obj, info, id):
    return get_pokemon(number=id)


@gqt.query.field('getPokemons')
def resolve_pokemons(obj, info, input):
    return get_pokemons(
        sort_input=input.get('sort'),
        filter_input=input.get('filter'),
        search_input=input.get('search'),
        pagination_input=input.get('pagination'),
    )
