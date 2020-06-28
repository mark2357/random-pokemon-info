'''contains function for retreving pokemon API Data'''

import json
import random

from ..helpers.fetch_data_from_api import fetch_data_from_api
from ..helpers.get_request_id_from_url import get_request_id_from_url

def get_pokemon_data(number):
    '''returns the data for the given pokemon with the given national dex number (works for 1 - 807)'''

    data = json.loads(fetch_data_from_api(f'https://pokeapi.co/api/v2/pokemon/{str(number)}'))
    return data

def get_random_pokemon_data():
    '''returns the data from a random pokemon'''

    url_list = get_pokemon_url_list(False)
    num = random.randrange(0, len(url_list))
    data = json.loads(fetch_data_from_api(url_list[num]))
    return data


def get_pokemon_url_list(get_forms):
    '''returns an array with the list containing all the urls for evolution chains'''

    data = json.loads(fetch_data_from_api('https://pokeapi.co/api/v2/pokemon/?limit=1000'))


    url_cache_list = []
    for item in data['results']:
        # if forms are meant to be included
        if get_forms:
            url_cache_list.append(item['url'])
        else:
            # if forms are not meant to be included determine id as forms has ids over 10000
            id_value = get_request_id_from_url(item['url'])

            if int(id_value) < 10000:
                url_cache_list.append(item['url'])

    return url_cache_list
