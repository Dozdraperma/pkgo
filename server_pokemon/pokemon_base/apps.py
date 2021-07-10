from django.apps import AppConfig


class PokemonBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pokemon_base'
