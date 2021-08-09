from ariadne import (
    QueryType,
    ObjectType
)

types = [
    query := QueryType(),
    pokemon := ObjectType('Pokemon'),
    evolution := ObjectType('Evolution')
]
