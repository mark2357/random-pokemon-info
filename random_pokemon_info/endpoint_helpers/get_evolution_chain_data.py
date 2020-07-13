'''contains function for retreving evolution chain API Data'''

import json
import random

from ..helpers.fetch_data_from_api import fetch_data_from_api

def get_pokemon_evolution_chain_data(number):
    '''returns the data for the given evolution chain (works for 1 - 427) if there is an error returns None'''

    url = f'https://pokeapi.co/api/v2/evolution-chain/{str(number)}'

    data = None
    try:
        data = json.loads(fetch_data_from_api(url))
        return data

    except json.decoder.JSONDecodeError:
        print(f'ERROR decoding json from {url} return data was {data}')
        return None


def get_random_evolution_chain_data():
    '''returns the data from a random pokemon evolution chain  if there is an error returns None'''

    url_list = get_evolution_chain_url_list()
    num = random.randrange(0, len(url_list))

    data = None
    try:
        data = json.loads(fetch_data_from_api(url_list[num]))
        return data

    except json.decoder.JSONDecodeError:
        print(f'ERROR decoding json from {url_list[num]} return data was {data}')
        return None



def get_evolution_chain_url_list():
    '''returns an array with the list containing all the urls for evolution chains'''

    url = 'https://pokeapi.co/api/v2/evolution-chain/?limit=500'
    data = None
    try:
        data = json.loads(fetch_data_from_api(url))

    except json.decoder.JSONDecodeError:
        print(f'ERROR decoding json from {url} return data was {data}')
        return None


    url_cache_list = []
    for item in data['results']:
        url_cache_list.append(item['url'])

    return url_cache_list
