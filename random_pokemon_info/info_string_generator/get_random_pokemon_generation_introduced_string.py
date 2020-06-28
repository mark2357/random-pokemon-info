'''contains function that returns string stating random pokemon name and the generation it was introduced'''

from ..endpoint_helpers.get_pokemon_species_data import get_random_pokemon_species_data

def get_random_pokemon_generation_introduced_string():
    '''returns string stating random pokemon name and the generation it was introduced'''
    data = get_random_pokemon_species_data()
    pokemon_name = data['name'].replace('-', ' ')
    generation_name = data['generation']['name']
    generation_name = generation_name.replace('-', ' ')

    return f'{pokemon_name} was introduced in {generation_name}'
