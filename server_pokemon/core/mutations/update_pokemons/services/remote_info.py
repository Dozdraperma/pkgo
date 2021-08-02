from typing import List, Dict, Union, Tuple, Optional

import demjson
import requests
from bs4 import BeautifulSoup

from core.mutations.update_pokemons.domain.remote import PokemonBaseInfo
from core.shared.domain.pokemon import Pokemon, Gender, Stage, Type
from core.shared.service.pokemon import PokemonRepository


class PokemonGameinfo(PokemonRepository):
    REMOTE_ROOT_URL = 'https://pokemon.gameinfo.io'
    REMOTE_DATA_URL = f'{REMOTE_ROOT_URL}/en/js/pokemon-home.js?v=55b79d'
    pokemon_types = {
        1: Type.NORMAL,
        2: Type.FIGHTING,
        3: Type.FLYING,
        4: Type.POISON,
        5: Type.GROUND,
        6: Type.ROCK,
        7: Type.BUG,
        8: Type.GHOST,
        9: Type.STEEL,
        10: Type.FIRE,
        11: Type.WATER,
        12: Type.GRASS,
        13: Type.ELECTRIC,
        14: Type.PSYCHIC,
        15: Type.ICE,
        16: Type.DRAGON,
        17: Type.DARK,
        18: Type.FAIRY,
    }

    @classmethod
    def _collect_raw_info(cls) -> List:
        request = requests.get(cls.REMOTE_DATA_URL)
        raw = request.text.lstrip('var pokemon_list=').rstrip(';')
        return demjson.decode(raw)

    @staticmethod
    def _clean_name(name: Optional[str]) -> Tuple[str, Optional[Gender]]:
        if '♀' in name:
            return name.replace('♀', ''), Gender.FEMALE
        if '♂' in name:
            return name.replace('♂', ''), Gender.MALE
        return name, None

    @classmethod
    def _collect_raw_pokemon_info(cls, number: int, name: str) -> Dict[str, Union[int, str]]:
        info = {}

        url = f'{cls.REMOTE_ROOT_URL}/en/pokemon/{number}-{name}'
        request = requests.get(url)
        parse_data = BeautifulSoup(
            request.content,
            features='html.parser'
        )

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
        info['base_defense'] = list(pokemon_stats[1].find_all('td'))[-1].text
        info['base_stamina'] = list(pokemon_stats[2].find_all('td'))[-1].text

        # Collect height and weight
        info['height'] = float(parse_data.find('td', text='Height').find_next_sibling().text.replace('m', '').strip())
        info['weight'] = float(parse_data.find('td', text='Weight').find_next_sibling().text.replace('kg', '').strip())

        return info

    def _get_pokemon(self, pokemon_base: PokemonBaseInfo):
        raw_info = self._collect_raw_pokemon_info(
            number=pokemon_base.number,
            name=pokemon_base.name,
        )
        return Pokemon(
            number=pokemon_base.number,
            name=pokemon_base.name,
            height=int(raw_info['height'] * 1000),
            weight=int(raw_info['weight'] * 1000),
            max_cp=pokemon_base.max_cp,
            base_attack=raw_info['base_attack'],
            base_defense=raw_info['base_defense'],
            base_stamina=raw_info['base_stamina'],
            primary_type=pokemon_base.primary_type,
            secondary_type=pokemon_base.secondary_type,
            stage=Stage(raw_info['stage']),
            evolves_from=self._clean_name(raw_info['evolves_from'])[0] if raw_info['evolves_from'] else None,
            evolve_gender=self._clean_name(raw_info['evolves_from'])[1] if raw_info['evolves_from'] else None,
            family_name=pokemon_base.family_name
        )

    def get_pokemons(self) -> List[Pokemon]:
        pokemon_info = self._collect_raw_info()

        base_info = [
            PokemonBaseInfo(
                number=number,
                generation=info[0],
                name=self._clean_name(info[1])[0],
                max_cp=info[4],
                primary_type=self.pokemon_types[info[5][0]],
                secondary_type=self.pokemon_types[info[5][1]] if len(info[5]) == 2 else None,
                family_name=list(pokemon_family[0].values())[0][1],
            )
            for pokemon_family in pokemon_info
            for pokemon in pokemon_family
            for number, info in pokemon.items()
        ]

        for pokemon in base_info:
            print(self._get_pokemon(pokemon))
            raise

        pokemons = [
            self._get_pokemon(pokemon)
            for pokemon in base_info
        ]
