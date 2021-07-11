import importlib
import pkgutil
from types import ModuleType
from typing import Dict

from ariadne import load_schema_from_path, make_executable_schema

import gql_api.resolvers as root_resolvers
import gql_api.resolvers.objects as object_resolvers
from gql_api.gql_api_types import types
from server_pokemon.settings import BASE_DIR

SCHEMA_PATH = BASE_DIR / 'gql_api' / 'schema.graphql'


def import_submodules(package, recursive: bool = True) -> Dict[str, ModuleType]:
    """
    Рекурсивно импортирует все модули в папке.
    :param package:
    :param recursive:
    :return:
    """

    if isinstance(package, str):
        package = importlib.import_module(package)
    elif not isinstance(package, ModuleType):
        raise TypeError('must provide a module path or an inported module')

    results = {}

    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name))

    return results


import_submodules(root_resolvers)
import_submodules(object_resolvers)

schema = load_schema_from_path(SCHEMA_PATH)
schema = make_executable_schema(schema, types)
