from django.core.management.base import BaseCommand
from django.conf import settings
from pokemon_base.pokedex_parser import pokedex_parser

pokedex_path = settings.BASE_DIR / 'pokedex.json'

class Command(BaseCommand):
    help = 'Updates database from json'

    def handle(self, *args, **options):
        pokedex_parser(pokedex_path)