import gql_api.gql_api_types as gqt
from pokemon_base.models import Pokemon


@gqt.pokemon.field('id')
def resolve_id(obj: Pokemon, info):
    return obj.id


@gqt.pokemon.field('name')
def resolve_name(obj: Pokemon, info):
    return obj.name


@gqt.pokemon.field('height')
def resolve_height(obj: Pokemon, info):
    return obj.height


@gqt.pokemon.field('weight')
def resolve_weight(obj: Pokemon, info):
    return obj.weight


@gqt.pokemon.field('maxCP')
def resolve_max_cp(obj: Pokemon, info):
    return obj.max_cp


@gqt.pokemon.field('familyName')
def resolve_family_name(obj: Pokemon, info):
    return obj.family_name


@gqt.pokemon.field('baseAttack')
def resolve_base_attack(obj: Pokemon, info):
    return obj.base_attack


@gqt.pokemon.field('baseDefense')
def resolve_base_defense(obj: Pokemon, info):
    return obj.base_defense


@gqt.pokemon.field('baseStamina')
def resolve_base_stamina(obj: Pokemon, info):
    return obj.base_stamina


@gqt.pokemon.field('primaryType')
def resolve_primary_type(obj: Pokemon, info):
    return obj.primary_type


@gqt.pokemon.field('secondaryType')
def resolve_secondary_type(obj: Pokemon, info):
    return obj.secondary_type or None


@gqt.pokemon.field('evolutionStage')
def resolve_evolution_stage(obj: Pokemon, info):
    return obj.stage


@gqt.pokemon.field('evolvesFrom')
def resolve_evolves_from(obj: Pokemon, info):
    return obj.evolves_from


@gqt.pokemon.field('evolveGender')
def resolve_evolve_gender(obj: Pokemon, info):
    return obj.evolve_gender


@gqt.pokemon.field('evolvesTo')
def resolve_evolves_to(obj: Pokemon, info):
    return obj.evolves_to.all()
