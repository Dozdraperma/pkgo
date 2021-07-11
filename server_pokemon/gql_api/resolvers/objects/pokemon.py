import gql_api.gql_api_types as gqt
from pokemon_base.models import Pokemon

@gqt.pokemon.field('id')
def resolve_id(obj: Pokemon, info):
    return obj.id

@gqt.pokemon.field('name')
def resolve_name(obj: Pokemon, info):
    return obj.name