import re
from functools import reduce
from html import unescape
from typing import Dict, List, Optional, Tuple, Union

import demjson
import requests
from bs4 import BeautifulSoup

from core.mutations.update_pokemons.domain.gameinfo import Generation, GenerationItem, PokemonBaseInfo
from core.shared.domain.pokemon import Type, Gender, Stage, Evolution, Pokemon
from core.shared.service.pokemon import PokemonRepository


class PokemonGameinfo(PokemonRepository):
    REMOTE_ROOT_URL = 'https://pokemon.gameinfo.io'
    REMOTE_DATA_URL = f'{REMOTE_ROOT_URL}/en/js/pokemon-home.js?v=55b79d'
    MAX_EVO_GENS = 3

    TYPES = {
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

    def __init__(self):
        self.branch_cache: Dict[str, List[Generation]] = {}

    def _write_to_cache(self, gens: List[Generation]) -> None:
        for gen in gens:
            for name in (pok.name for pok in gen.pokemons):
                self.branch_cache[name] = gens

    @classmethod
    def collect_raw_info(cls) -> List:
        request = requests.get(cls.REMOTE_DATA_URL)
        raw = request.text.lstrip('var pokemon_list=').rstrip(';')
        return demjson.decode(raw)

    @classmethod
    def _resolve_gender(cls, pokemon: BeautifulSoup) -> Optional[Gender]:
        if 'male' in pokemon['class']:
            return Gender.MALE
        if 'female' in pokemon['class']:
            return Gender.FEMALE

    @staticmethod
    def _clean_name(name: str) -> str:
        to_exclude = ('♀', '♂', '&#039;')
        return reduce(lambda string, sym: string.replace(sym, ''), to_exclude, name)

    def _collect_evolutions(self, data: BeautifulSoup) -> List[Optional[Generation]]:
        url_pattern = r'\/(\d{1,3})-(\w+)'
        evolutions = []

        # Find branches in parse data
        branches = data.find_all(
            'div',
            attrs={
                'class': 'branch',
            }
        )

        # ToDo: Collect all branches
        for branch in branches:
            if any(
                    'active' in link['class']
                    for link in branch.find_all('a')
            ):
                evolutions = branch.find_all(
                    'div',
                    attrs={
                        'class': 'gen'
                    }
                )

        # Find number and name pokemon in evolutions, strip by max evolutions
        return [
            Generation(
                pokemons=[
                    GenerationItem(
                        id=int(re.search(url_pattern, pokemon['href'])[1]),
                        name=pokemon.find('div', attrs={'class': 'name'}).text,
                        required_gender=self._resolve_gender(pokemon)
                    )
                ],
                stage=Stage(i)
            )
            for i, generation in enumerate(evolutions[:self.MAX_EVO_GENS])
            for pokemon in generation.find_all('a')
        ]

    def _resolve_evolution(self, data: BeautifulSoup, name: str) -> Tuple[Optional[Evolution], Stage]:
        # Find generations
        generations = self._collect_evolutions(data)

        if not generations:
            return None, Stage(0)

        for i, generation in enumerate(generations):
            for pokemon in generation.pokemons:
                if pokemon.name == unescape(name):
                    if i == 0:
                        return None, generation.stage

                    past_generation = generations[i - 1]

                    if (count := len(past_generation.pokemons)) > 1:
                        raise ValueError(f'past branch of pokemon {name} contains {count} pokemons')

                    return Evolution(
                        id=past_generation.pokemons[0].id,
                        name=past_generation.pokemons[0].name,
                        gender=pokemon.required_gender
                    ), generation.stage

    def _collect_raw_pokemon_info(self, number: int, name: str) -> Dict[str, Union[int, str]]:
        info = {}

        url = f'{self.REMOTE_ROOT_URL}/en/pokemon/{number}-{name}'

        request = requests.get(url)
        parse_data = BeautifulSoup(
            request.content,
            features='html.parser'
        )

        # Find evolves from and stage
        info['evolves_from'], info['stage'] = self._resolve_evolution(parse_data, name)

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

    def get_pokemon(self, pokemon_base: PokemonBaseInfo) -> Pokemon:
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
            stage=raw_info['stage'],
            evolves_from=raw_info['evolves_from'],
            family_name=pokemon_base.family_name
        )
