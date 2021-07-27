from typing import Dict

from django.db.models import QuerySet


def sort_pokemon(sort_info: Dict, query: QuerySet):
    query = query.order_by(*sort_info['sort_by'])
    return query
