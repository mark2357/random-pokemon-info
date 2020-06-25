'''prints to console random information about pokemon using web API'''

import random

import info_string_generator

def get_random_info():
    '''returns string with random pokemon info'''
    # array is used to define which functions can be called and what the chance is
    functions_list = [
        {'weight': 1, 'func': info_string_generator.get_random_pokemon_ability_string},
        {'weight': 1, 'func': info_string_generator.get_random_pokemon_evolution_string},
        {'weight': 1, 'func': info_string_generator.get_random_pokemon_generation_introduced_string},
        {'weight': 1, 'func': info_string_generator.get_random_pokemon_height_string},
        {'weight': 1, 'func': info_string_generator.get_random_pokemon_highest_stat_string},
        {'weight': 1, 'func': info_string_generator.get_random_pokemon_lowest_stat_string},
        {'weight': 1, 'func': info_string_generator.get_random_pokemon_type_string},
        {'weight': 1, 'func': info_string_generator.get_random_pokemon_type_weekness_or_resistance_string},
        {'weight': 1, 'func': info_string_generator.get_random_pokemon_weight_string},
    ]

    total_weight = 0

    for func in functions_list:
        total_weight += func['weight']

    num = random.randrange(0, total_weight)

    current_weight = 0
    for func in functions_list:
        if current_weight + func['weight'] > num:
            return func['func']()
        else:
            current_weight += func['weight']
