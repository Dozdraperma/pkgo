from django.conf import settings
from django.http import HttpResponse

from pokemon_base.models import Pokemon
from pokemon_base.pokedex_parser import pokedex_parser


def test_page(request):
    print(Pokemon.objects.get(id=2).evolves_from)
    return HttpResponse('test')
