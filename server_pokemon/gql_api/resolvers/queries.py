from ariadne import convert_kwargs_to_snake_case
from django.db.models import Q

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


@gqt.query.field('searchPokemons')
@convert_kwargs_to_snake_case
def resolve_search_pokemons(*_, search):
    if dex := search.get('id'):
        return Pokemon.objects.filter(id__exact=dex).all()

    if name_input := search.get('name'):
        name = name_input['name']
        query_filter = Q(name__icontains=name)

        if name_input['include_evolutions']:
            query_filter = (
                    query_filter
                    | Q(evolves_from__name__icontains=name)
                    | Q(evolves_from__evolves_from__name__icontains=name)
                    | Q(evolves_to__name__icontains=name)
                    | Q(evolves_to__evolves_to__name__icontains=name)
            )

        return Pokemon.objects.filter(query_filter) or None

    if pok_type := search.get('type'):
        return Pokemon.objects.filter(
            Q(primary_type__iexact=pok_type)
            | Q(secondary_type__iexact=pok_type)
        )
