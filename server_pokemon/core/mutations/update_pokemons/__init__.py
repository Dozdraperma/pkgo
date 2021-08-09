from core.shared.actions.save import save_pokemons
from core.shared.service.pokemon import PokemonRepository
from server_pokemon import settings

VALIDATION_RESULT_PATH = settings.BASE_DIR / 'logs'
VALIDATION_RESULT_PATH.mkdir(parents=True, exist_ok=True)


def update_pokemons(
        repository: PokemonRepository,
) -> None:
    save_pokemons(repository.get_pokemons())
