'''contains function that returns string stating random pokemon name and it's weight'''

from endpoint_helpers.get_pokemon_data import get_random_pokemon_data

def get_random_pokemon_weight_string():
    '''returns string stating random pokemon name and it's weight'''
    data = get_random_pokemon_data()
    name = data['name']
    weight = data['weight']
    return f'{name} has a weight of {weight / 10} kg'
