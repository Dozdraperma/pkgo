import gql_api.gql_api_types as gqt
from core.queries.evolution import get_pokemon_evolutions
from core.shared.domain.pokemon import Pokemon


@gqt.pokemon.field('id')
def resolve_id(obj: Pokemon, info):
    return obj.number


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
    return obj.primary_type.value


@gqt.pokemon.field('secondaryType')
def resolve_secondary_type(obj: Pokemon, info):
    return obj.secondary_type.value if obj.secondary_type else None


@gqt.pokemon.field('evolution')
def resolve_evolves_from(obj: Pokemon, info):
    return get_pokemon_evolutions(obj)


@gqt.pokemon.field('description')
def resolve_description(obj: Pokemon, info):
    return obj.description

# @gqt.pokemon.field('evolutionBranch')
# def resolve_evolution_branch(obj: Pokemon, info):
#     return {
#         '__typename': 'Branch',
#         'stages': [
#             {
#                 '__typename': 'EvolutionStage',
#                 'stageCount': stage.stage_count,
#                 'pokemons': stage.pokemons
#             }
#             for stage in get_evolution_branch(obj).stages
#         ]
#     }
