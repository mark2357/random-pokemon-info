'''contains function for retreving evolution chain API Data'''

import json
import random

from generic.fetch_data_from_api import fetch_data_from_api

def get_pokemon_evolution_chain_data(number):
    '''returns the data for the given evolution chain (works for 1 - 427)'''
    # validate number
    if number < 0:
        print('number "' + number + '" is not valid it must be a number larger than 0')
        return None
    elif number > 427:
        print('number "' + number + '" is not valid it must be a number less than 808')
        return None

    data = json.loads(fetch_data_from_api(f'https://pokeapi.co/api/v2/evolution-chain/{str(number)}'))
    return data

def get_random_evolution_chain_data():
    '''returns the data from a random pokemon evolution chain'''
    num = random.randrange(1, 428)
    data = get_pokemon_evolution_chain_data(num)
    return data
