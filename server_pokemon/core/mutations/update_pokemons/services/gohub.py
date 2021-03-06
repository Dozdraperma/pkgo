from typing import Dict, Optional, Set, List

import requests
from pydantic import ValidationError

from core.shared.domain.pokemon import Pokemon, Type, PokemonBaseInfo, Evolution, Gender
from core.shared.service.log import logger
from core.shared.service.pokemon import PokemonRepository


class PokemonGOHub(PokemonRepository):
    REMOTE_ROOT_URL = 'https://db.pokemongohub.net'
    GENERATIONS = 8
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Alt-Used": "db.pokemongohub.net",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-origin"
    }

    def get_pokemon_list_by_generation(self, generation: int):
        request = requests.get(
            url=f'{self.REMOTE_ROOT_URL}/api/pokemon/with-generation/{generation}?locale=en-US',
            headers=self.HEADERS
        )

        return request.json()

    def get_pokemon_list(self):
        pokemons = []
        for gen in range(1, self.GENERATIONS + 1):
            pokemons += self.get_pokemon_list_by_generation(gen)

        return {
            PokemonBaseInfo(number=pokemon['id'], name=pokemon['name'])
            for pokemon in pokemons
        }

    def get_evolution(self, name: str, raw_evolutions: List[Dict]) -> Optional[Evolution]:
        if not raw_evolutions:
            return

        for evolution in raw_evolutions:
            if evolution['evolutionName'] == name:
                return Evolution(
                    id=evolution['pokemonPokedexId'],
                    name=evolution['pokemonName'],
                    gender=evolution['genderRequirement'] and Gender(evolution['genderRequirement'].title())
                )

    def _get_raw_pokemon(self, number: int, form='') -> Optional[Dict]:
        request = requests.get(
            url=f'{self.REMOTE_ROOT_URL}/api/pokemon/{number}?locale=en-US&form={form}',
            headers=self.HEADERS
        )

        return request.json()

    def get_pokemon(self, number: int) -> Optional[Pokemon]:
        raw = self._get_raw_pokemon(number)
        if raw is None:
            raw = self._get_raw_pokemon(number, form='Normal')
        if raw is None:
            return

        logger.info(f'Processing {raw["name"]}')

        try:
            return Pokemon(
                number=raw['id'],
                name=raw['name'],
                height=raw['height'],
                weight=raw['weight'],
                max_cp=raw['maxcp'],
                base_attack=raw['atk'],
                base_defense=raw['def'],
                base_stamina=raw['sta'],
                primary_type=Type(raw['type1'].title()),
                secondary_type=raw['type2'] and Type(raw['type2'].title()),
                evolves_from=self.get_evolution(raw['name'], raw['evolutionLine']),
                description=raw['description'],
                family_name=raw['family'][0]['name'] if raw['family'] else raw['name']
            )
        except ValidationError as err:
            failures = {
                error['loc'][0]
                for error in err.errors()
            }
            logger.info(f'Validation failed: {failures}')

    def get_pokemons(self) -> Set[Pokemon]:
        pokemons = {
            self.get_pokemon(pokemon.number)
            for pokemon in self.get_pokemon_list()
        }
        pokemons = {x for x in pokemons if x is not None}

        return pokemons
