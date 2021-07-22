from ariadne import convert_kwargs_to_snake_case
from django.db.models import Q

import gql_api.gql_api_types as gqt
from gql_api.resolvers.queries.sort import sort_pokemon
from pokemon_base.models import Pokemon


@gqt.query.field('searchPokemons')
@convert_kwargs_to_snake_case
def resolve_search_pokemons(*_, search):
    query = Pokemon.objects.all()
    if dex := search.get('id'):
        query = Pokemon.objects.filter(id__exact=dex).all()

    if name := search.get('name'):
        query_filter = Q(name__icontains=name)

        if search['include_evolutions']:
            query_filter = (
                    query_filter
                    | Q(evolves_from__name__icontains=name)
                    | Q(evolves_from__evolves_from__name__icontains=name)
                    | Q(evolves_to__name__icontains=name)
                    | Q(evolves_to__evolves_to__name__icontains=name)
            )

        query = Pokemon.objects.filter(query_filter) or None

    if pok_type := search.get('type'):
        query = Pokemon.objects.filter(
            Q(primary_type__iexact=pok_type)
            | Q(secondary_type__iexact=pok_type)
        )

    if sort := search.get('sort'):
        query = sort_pokemon(sort, query)

    return query
