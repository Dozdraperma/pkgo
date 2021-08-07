from django.conf import settings
from django.core.management.base import BaseCommand

from core.mutations.update_pokemons import update_pokemons
from core.mutations.update_pokemons.services.gohub import PokemonGOHub

pokedex_path = settings.BASE_DIR / 'pokedex.json'


class Command(BaseCommand):
    help = 'Updates database from json'

    def handle(self, *args, **options):
        update_pokemons(
            repository=PokemonGOHub()
        )
