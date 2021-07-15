from ariadne import convert_kwargs_to_snake_case

import gql_api.gql_api_types as gqt
from gql_api.resolvers.queries.sort import sort_pokemon
from pokemon_base.models import Pokemon


@gqt.query.field('hello')
def resolve_hello(*_):
    return 'Hello from pokedex!'


@gqt.query.field('getPokemon')
@convert_kwargs_to_snake_case
def resolve_pokemon(obj, info, id):
    return Pokemon.objects.get(id=id)


@gqt.query.field('getPokemons')
@convert_kwargs_to_snake_case
def resolve_pokemons(*_, sort):
    query = Pokemon.objects
    if sort:
        query = sort_pokemon(sort, query)
    return query.all()
