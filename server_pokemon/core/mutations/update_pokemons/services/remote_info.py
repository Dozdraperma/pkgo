import enum
from abc import ABC, abstractmethod
from pprint import pprint
from typing import List, Dict
from bs4 import BeautifulSoup

from core.shared.domain.pokemon import Pokemon
from core.shared.service.pokemon import PokemonRepository

import demjson

import requests

from core.mutations.update_pokemons.domain.remote import PokemonBaseInfo, Type


class PokemonGameinfo(PokemonRepository):
    REMOTE_ROOT_URL = 'https://pokemon.gameinfo.io'
    REMOTE_DATA_URL = f'{REMOTE_ROOT_URL}/en/js/pokemon-home.js?v=55b79d'

    @classmethod
    def _collect_raw_info(cls) -> List:
        request = requests.get(cls.REMOTE_DATA_URL)
        raw = request.text.lstrip('var pokemon_list=').rstrip(';')
        return demjson.decode(raw)

    @classmethod
    def _collect_raw_pokemon_info(cls, number: int, name: str) -> Dict:
        url = f'{cls.REMOTE_ROOT_URL}/en/pokemon/{number}-{name}'
        request = requests.get(url)
        parse_data = BeautifulSoup(request.content)
        evo_branch = parse_data.find(
            'div',
            attrs={
                'class': 'branch'
            }
        )
        pprint(evo_branch.children)

    def _get_pokemon(self, pokemon_base: PokemonBaseInfo):
        pass

    def get_pokemons(self) -> List[Pokemon]:
        pokemon_info = self._collect_raw_info()

        base_info = [
            PokemonBaseInfo(
                number=number,
                generation=info[0],
                name=info[1],
                max_cp=info[4],
                primary_type=Type(info[5][0]),
                secondary_type=Type(info[5][1]) if len(info[5]) == 2 else None
            )
            for pokemon_family in pokemon_info
            for pokemon in pokemon_family
            for number, info in pokemon.items()
        ]
