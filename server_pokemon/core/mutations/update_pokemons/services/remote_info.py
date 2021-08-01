from typing import List, Dict, Union

import demjson
import requests
from bs4 import BeautifulSoup

from core.mutations.update_pokemons.domain.remote import PokemonBaseInfo, Type
from core.shared.domain.pokemon import Pokemon
from core.shared.service.pokemon import PokemonRepository


class PokemonGameinfo(PokemonRepository):
    REMOTE_ROOT_URL = 'https://pokemon.gameinfo.io'
    REMOTE_DATA_URL = f'{REMOTE_ROOT_URL}/en/js/pokemon-home.js?v=55b79d'

    @classmethod
    def _collect_raw_info(cls) -> List:
        request = requests.get(cls.REMOTE_DATA_URL)
        raw = request.text.lstrip('var pokemon_list=').rstrip(';')
        return demjson.decode(raw)

    @classmethod
    def _collect_raw_pokemon_info(cls, number: int, name: str) -> Dict[str, Union[int, str]]:
        info = {}

        url = f'{cls.REMOTE_ROOT_URL}/en/pokemon/{number}-{name}'
        request = requests.get(url)
        parse_data = BeautifulSoup(request.content)

        evo_branch = parse_data.find(
            'div',
            attrs={
                'class': 'branch'
            }
        )
        name = name.title()
        evo_pokemons = [children.find('div', attrs={'class': 'name'}).text for children in evo_branch.children]

        # Find evolves from
        if name not in evo_pokemons:
            raise ValueError(f'{name} not in {evo_pokemons}!')
        if evo_pokemons.index(name) == 0:
            info['evolves_from'] = None
        else:
            info['evolves_from'] = evo_pokemons[evo_pokemons.index(name) - 1]

        # Find evolve stage
        info['stage'] = evo_pokemons.index(name) + 1

        # Collect pokemon stats
        pokemon_stats = parse_data.find(
            'table',
            attrs={
                'class': 'table-stats'
            }
        ).find_all('tr')
        info['base_attack'] = list(pokemon_stats[0].find_all('td'))[-1].text
        info['base_defence'] = list(pokemon_stats[1].find_all('td'))[-1].text
        info['base_stamina'] = list(pokemon_stats[2].find_all('td'))[-1].text

        # Collect height and weight
        info['height'] = int(parse_data.find('td', text='Height').find_next_sibling().text.replace('m', '').strip()) * 10
        info['weight'] = int(parse_data.find('td', text='Weight').find_next_sibling().text.replace('kg', '').strip()) * 1000

        return info

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
