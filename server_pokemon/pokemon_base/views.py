from django.shortcuts import render
from django.http import HttpResponse
from pokemon_base.pokedex_parser import pokedex_parser


def test_page(request):
    pokedex_parser()
    return HttpResponse('test')
