from django.contrib import admin
from pokemon_base.models import Pokemon


# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_primary_type', 'get_secondary_type', 'get_evolves_from')
    list_display_links = ('id', 'name')
    ordering = ('id', )

    def get_primary_type(self, obj: Pokemon):
        return obj.get_primary_type_display()

    def get_secondary_type(self, obj: Pokemon):
        return obj.get_secondary_type_display()

    def get_evolves_from(self, obj: Pokemon):
        return obj.evolves_from.name if obj.evolves_from else None

    get_primary_type.short_description = 'Primary type'
    get_secondary_type.short_description = 'Secondary type'
    get_evolves_from.short_description = 'Evolves from'

