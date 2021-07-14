from ariadne import convert_kwargs_to_snake_case

import gql_api.gql_api_types as gqt
from pokemon_base.models import Pokemon


@gqt.query.field('hello')
def resolve_hello(*_):
    return 'Hello from pokedex!'


@convert_kwargs_to_snake_case
@gqt.query.field('getPokemon')
def resolve_pokemon(obj, info, id):
    return Pokemon.objects.get(id=id)

@gqt.query.field('getPokemons')
def resolve_pokemons(*_):
    return Pokemon.objects.all()