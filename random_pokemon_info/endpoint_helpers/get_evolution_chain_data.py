'''contains function for retreving evolution chain API Data'''

import json
import random

from ..helpers.fetch_data_from_api import fetch_data_from_api

def get_pokemon_evolution_chain_data(number):
    '''returns the data for the given evolution chain (works for 1 - 427)'''

    data = json.loads(fetch_data_from_api(f'https://pokeapi.co/api/v2/evolution-chain/{str(number)}'))
    return data


def get_random_evolution_chain_data():
    '''returns the data from a random pokemon evolution chain'''

    url_list = get_evolution_chain_url_list()
    num = random.randrange(0, len(url_list))
    data = json.loads(fetch_data_from_api(url_list[num]))
    return data


def get_evolution_chain_url_list():
    '''returns an array with the list containing all the urls for evolution chains'''

    data = json.loads(fetch_data_from_api('https://pokeapi.co/api/v2/evolution-chain/?limit=500'))

    url_cache_list = []
    for item in data['results']:
        url_cache_list.append(item['url'])

    return url_cache_list