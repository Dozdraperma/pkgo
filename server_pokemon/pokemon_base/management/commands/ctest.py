from django.core.management.base import BaseCommand

from core.mutations.update_pokemons.services.gohub import PokemonGOHub


class Command(BaseCommand):
    help = 'Custom test'

    #
    # def add_arguments(self, parser: argparse.ArgumentParser):
    #     parser.add_argument(
    #         'identity',
    #         nargs='+'
    #     )

    def handle(self, *args, **options):
        pok = PokemonGOHub().get_pokemon(386)
        print(pok)
