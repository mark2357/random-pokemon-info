'''contains function that returns string stating random pokemon name and one of it's weeknesses resistances or immunities'''

import random

from endpoint_helpers.get_pokemon_data import get_random_pokemon_data
from endpoint_helpers.get_type_data import get_type_weeknesses_and_resistances
from endpoint_helpers.get_type_data import get_duel_type_weeknesses_and_resistances

def get_random_pokemon_type_weekness_or_resistance_string():
    '''returns string stating random pokemon name and one of it's weeknesses resistances or immunities'''
    data = get_random_pokemon_data()
    name = data['name']
    types = data['types']

    damage_multipliers = None
    # single type pokemon
    if len(types) == 1:
        type_name = types[0]['type']['name']
        damage_multipliers = get_type_weeknesses_and_resistances(type_name)

    # double type pokemon
    elif len(types) == 2:
        type_name_1 = types[0]['type']['name']
        type_name_2 = types[1]['type']['name']
        damage_multipliers = get_duel_type_weeknesses_and_resistances(type_name_1, type_name_2)


    if damage_multipliers is not None:
        type_name = random.choice(list(damage_multipliers.keys()))
        type_multiplier = damage_multipliers[type_name]

        if type_multiplier == 0:
            return f'{name} is immune to {type_name} type moves'
        elif type_multiplier == 0.25:
            return f'{name} is double resistant to {type_name} type moves'
        elif type_multiplier == 0.5:
            return f'{name} is resistant to {type_name} type moves'
        elif type_multiplier == 2:
            return f'{name} is weak to {type_name} type moves'
        elif type_multiplier == 4:
            return f'{name} is double weak to {type_name} type moves'