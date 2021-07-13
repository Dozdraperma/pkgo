import gql_api.gql_api_types as gqt
from pokemon_base.models import Pokemon


@gqt.pokemon.field('id')
def resolve_id(obj: Pokemon, info):
    return obj.id


@gqt.pokemon.field('name')
def resolve_name(obj: Pokemon, info):
    return obj.name


@gqt.pokemon.field('height')
def resolve_name(obj: Pokemon, info):
    return obj.height


@gqt.pokemon.field('weight')
def resolve_name(obj: Pokemon, info):
    return obj.weight


@gqt.pokemon.field('maxCP')
def resolve_name(obj: Pokemon, info):
    return obj.max_cp


@gqt.pokemon.field('familyName')
def resolve_name(obj: Pokemon, info):
    return obj.family_name


@gqt.pokemon.field('baseAttack')
def resolve_name(obj: Pokemon, info):
    return obj.base_attack


@gqt.pokemon.field('baseDefense')
def resolve_name(obj: Pokemon, info):
    return obj.base_defense


@gqt.pokemon.field('baseStamina')
def resolve_name(obj: Pokemon, info):
    return obj.base_stamina


@gqt.pokemon.field('primaryType')
def resolve_name(obj: Pokemon, info):
    return obj.primary_type


@gqt.pokemon.field('secondaryType')
def resolve_name(obj: Pokemon, info):
    return obj.secondary_type


@gqt.pokemon.field('evolutionStage')
def resolve_name(obj: Pokemon, info):
    return obj.stage


@gqt.pokemon.field('evolvesFrom')
def resolve_name(obj: Pokemon, info):
    return obj.evolves_from


@gqt.pokemon.field('evolveGender')
def resolve_name(obj: Pokemon, info):
    return obj.evolve_gender
