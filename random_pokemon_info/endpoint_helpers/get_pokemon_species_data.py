'''contains function for retreving pokemon API Data'''

import json
import random

from ..helpers.fetch_data_from_api import fetch_data_from_api

def get_pokemon_species_data(number):
    '''returns the species data for the given pokemon with the given national dex number (works for 1 - 807)'''

    # validate number
    if number < 0:
        print('number "' + number + '" is not valid it must be a number larger than 0')
        return None
    elif number > 807:
        print('number "' + number + '" is not valid it must be a number less than 808')
        return None

    data = json.loads(fetch_data_from_api(f'https://pokeapi.co/api/v2/pokemon-species/{str(number)}'))
    return data

def get_random_pokemon_species_data():
    '''returns the species data from a random pokemon'''

    num = random.randrange(1, 808)
    data = get_pokemon_species_data(num)
    return data
