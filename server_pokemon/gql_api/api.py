import importlib
import pkgutil
from types import ModuleType

from ariadne import load_schema_from_path, make_executable_schema

import gql_api.resolvers.objects as object_resolvers
import gql_api.resolvers.queries as query_resolvers
from gql_api.gql_api_types import types
from server_pokemon.settings import BASE_DIR

SCHEMA_PATH = BASE_DIR / 'gql_api' / 'schema.graphql'


def import_submodules(package, recursive: bool = True) -> None:
    """
    Рекурсивно импортирует все модули в папке.
    """

    if isinstance(package, str):
        package = importlib.import_module(package)
    elif not isinstance(package, ModuleType):
        raise TypeError('must provide a module path or an imported module')

    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__, package.__name__ + '.'):
        importlib.import_module(name)
        if recursive and is_pkg:
            import_submodules(package=name)


import_submodules(query_resolvers)
import_submodules(object_resolvers)

schema = load_schema_from_path(SCHEMA_PATH)
schema = make_executable_schema(schema, types)
