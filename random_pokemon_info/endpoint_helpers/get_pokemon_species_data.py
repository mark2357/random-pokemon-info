'''contains function for retreving pokemon API Data'''

import json
import random

from ..helpers.fetch_data_from_api import fetch_data_from_api

def get_pokemon_species_data(number):
    '''returns the species data for the given pokemon with the given national dex number (works for 1 - 807)'''

    data = json.loads(fetch_data_from_api(f'https://pokeapi.co/api/v2/pokemon-species/{str(number)}'))
    return data


def get_random_pokemon_species_data():
    '''returns the species data from a random pokemon'''

    url_list = get_pokemon_species_url_list()
    num = random.randrange(0, len(url_list))
    data = json.loads(fetch_data_from_api(url_list[num]))
    return data


def get_pokemon_species_url_list():
    '''returns an array with the list containing all the urls for pokemon species data'''

    data = json.loads(fetch_data_from_api('https://pokeapi.co/api/v2/pokemon-species/?limit=1000'))

    url_cache_list = []
    for item in data['results']:
        url_cache_list.append(item['url'])

    return url_cache_list
