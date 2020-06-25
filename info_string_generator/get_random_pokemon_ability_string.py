'''contains function that returns string stating random pokemon name and one of it's possible abilities'''

import random

from endpoint_helpers.get_pokemon_data import get_random_pokemon_data

def get_random_pokemon_ability_string():
    '''returns string stating random pokemon name and one of it's possible abilities'''
    data = get_random_pokemon_data()
    name = data['name'].replace('-', ' ')
    abilities = data['abilities']

    ability_data = abilities[random.randrange(0, len(abilities))]
    ability_name = ability_data['ability']['name'].replace('-', ' ')

    if ability_data['is_hidden']:
        return f'{name} can have the hidden ability {ability_name}'
    else:
        return f'{name} can have the ability {ability_name}'
