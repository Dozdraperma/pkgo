from django.core.management.base import BaseCommand
from django.conf import settings

from core.mutations.update_pokemons.services.remote_info import PokemonGameinfo
from pokemon_base.pokedex_parser import pokedex_parser


class Command(BaseCommand):
    help = 'Custom test'

    def handle(self, *args, **options):
        PokemonGameinfo()._collect_raw_pokemon_info(2, 'ivysaur')