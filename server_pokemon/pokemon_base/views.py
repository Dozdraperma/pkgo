from django.http import HttpResponse

from pokemon_base.models import Pokemon


def test_page(request):
    print(Pokemon.objects.get(id=2).evolves_from)
    return HttpResponse('test')
