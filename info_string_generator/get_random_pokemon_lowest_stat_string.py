'''contains function that returns string stating random pokemon name and it's lowest stat'''

from endpoint_helpers.get_pokemon_data import get_random_pokemon_data

def get_random_pokemon_lowest_stat_string():
    '''returns string stating random pokemon name and it's lowest stat'''

    data = get_random_pokemon_data()
    name = data['name'].replace('-', ' ')

    lowest_stat_value = 256
    lowest_stat_name = ''
    for stat in data['stats']:
        if stat['base_stat'] < lowest_stat_value:
            lowest_stat_value = stat['base_stat']
            lowest_stat_name = stat['stat']['name'].replace('-', ' ')

    return f'{name} lowest stat is {lowest_stat_name}'
    