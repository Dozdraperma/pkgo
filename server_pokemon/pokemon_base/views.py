from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from pokemon_base.pokedex_parser import pokedex_parser


def test_page(request):
    pokedex_path = settings.BASE_DIR / 'pokedex.json'
    pokedex_parser(pokedex_path)
    return HttpResponse('test')
