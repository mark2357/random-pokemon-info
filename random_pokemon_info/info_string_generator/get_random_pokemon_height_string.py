'''contains function that returns string starting random pokemon name '''

from ..endpoint_helpers.get_pokemon_data import get_random_pokemon_data

def get_random_pokemon_height_string():
    '''returns string stating random pokemon name and it's height'''
    data = get_random_pokemon_data()
    name = data['name'].replace('-', ' ')
    height = data['height']
    return f'{name} has a height of {height / 10} m'
