from typing import Dict

from ariadne import convert_kwargs_to_snake_case
from django.db.models import QuerySet


def sort_pokemon(sort_info: Dict, query: QuerySet):
    for sort_type in sort_info['sort_by']:
        query = query.order_by(sort_type)
    return query
