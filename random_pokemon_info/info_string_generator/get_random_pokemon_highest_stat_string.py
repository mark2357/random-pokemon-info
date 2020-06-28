'''contains function that returns string stating random pokemon name and it's highest stat'''

from ..endpoint_helpers.get_pokemon_data import get_random_pokemon_data

def get_random_pokemon_highest_stat_string():
    '''returns string stating random pokemon name and it's highest stat'''

    data = get_random_pokemon_data()
    name = data['name'].replace('-', ' ')

    highest_stat_value = 0
    highest_stat_name = ''

    for stat in data['stats']:
        if stat['base_stat'] > highest_stat_value:
            highest_stat_value = stat['base_stat']
            highest_stat_name = stat['stat']['name'].replace('-', ' ')

    return f'{name} highest stat is {highest_stat_name}'
