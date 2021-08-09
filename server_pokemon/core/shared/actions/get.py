import pokemon_base.models as db
from core.shared.domain.pokemon import Pokemon, Type, Evolution, Gender


def get_pokemon(number: int) -> Pokemon:
    db_pokemon = db.Pokemon.objects.get(pk=number)
    return Pokemon(
        number=db_pokemon.pk,
        name=db_pokemon.name,
        height=db_pokemon.height / 1000,
        weight=db_pokemon.weight / 1000,
        max_cp=db_pokemon.max_cp,
        base_attack=db_pokemon.base_attack,
        base_defense=db_pokemon.base_defense,
        base_stamina=db_pokemon.base_stamina,
        primary_type=Type(db_pokemon.primary_type),
        secondary_type=Type(db_pokemon.secondary_type) if db_pokemon.secondary_type else None,
        evolves_from=Evolution(
            id=db_pokemon.evolves_from_id,
            name=db_pokemon.evolves_from.name,
            gender=db_pokemon.evolve_gender
        ) if db_pokemon.evolves_from else None,
        family_name=db_pokemon.family_name,
    )


def convert_pokemon(db_pokemon: db.Pokemon) -> Pokemon:
    return Pokemon(
        number=db_pokemon.pk,
        name=db_pokemon.name,
        height=db_pokemon.height / 1000,
        weight=db_pokemon.weight / 1000,
        max_cp=db_pokemon.max_cp,
        base_attack=db_pokemon.base_attack,
        base_defense=db_pokemon.base_defense,
        base_stamina=db_pokemon.base_stamina,
        primary_type=Type(db_pokemon.primary_type),
        secondary_type=Type(db_pokemon.secondary_type) if db_pokemon.secondary_type else None,
        evolves_from=Evolution(
            id=db_pokemon.evolves_from_id,
            name=db_pokemon.evolves_from.name,
            gender=db_pokemon.evolve_gender and Gender(db_pokemon.evolve_gender.split('.')[-1].lower().title())
        ) if db_pokemon.evolves_from else None,
        family_name=db_pokemon.family_name,
    )
