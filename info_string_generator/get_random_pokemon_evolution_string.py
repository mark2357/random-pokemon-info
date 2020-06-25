'''contains function that returns string stating random pokemon and if it evolves from or to another pokemon'''

import random

from endpoint_helpers.get_evolution_chain_data import get_random_evolution_chain_data

def get_random_pokemon_evolution_string():
    '''returns string stating random pokemon and if it evolves from or to another pokemon'''

    data = get_random_evolution_chain_data()
    evolution_chain_names = []

    add_evolution_chain_name_to_array(evolution_chain_names, data['chain'])

    return_string = ''

    # pokemon doesn't evolve
    if len(evolution_chain_names) == 1:
        return_string = f"{evolution_chain_names[0]['pokemon_name']} doesn't evolve"
    # pokemon eveles once
    elif len(evolution_chain_names) == 2:
        return_string = f"{evolution_chain_names[0]['pokemon_name']} evolves into {evolution_chain_names[1]['pokemon_name']}"
        return_string = add_evolution_method(return_string, evolution_chain_names[0])
    # pokemon evolves multiple times
    elif len(evolution_chain_names) == 3:
        # should be 0 or 1
        random_index = random.randrange(0, 2)
        return_string = f"{evolution_chain_names[random_index]['pokemon_name']} evolves into {evolution_chain_names[random_index + 1]['pokemon_name']}"
        return_string = add_evolution_method(return_string, evolution_chain_names[random_index])

    return return_string


def add_evolution_chain_name_to_array(array, evolution_data):
    '''recursively adds pokemon names to array'''

    pokemon_data = {}
    pokemon_data['pokemon_name'] = evolution_data['species']['name'].replace('-', ' ')
    possible_evolution_count = len(evolution_data['evolves_to'])
    if possible_evolution_count > 0:
        random_evolution_index = random.randrange(0, possible_evolution_count)

        evolution_info = evolution_data['evolves_to'][random_evolution_index]

        if evolution_info['evolution_details'][0]['trigger']['name'] == 'level-up' and evolution_info['evolution_details'][0]['min_level'] is not None:
            pokemon_data['pokemon_evolves_level'] = evolution_info['evolution_details'][0]['min_level']

        array.append(pokemon_data)

        add_evolution_chain_name_to_array(array, evolution_info)
    else:
        array.append(pokemon_data)


def add_evolution_method(string_to_append, pokemon_info):
    '''appends extra info on how evolution occurs if it is one of the supported options (currently only level up is supported)'''
    if 'pokemon_evolves_level' in pokemon_info:
        string_to_append += f" at level {pokemon_info['pokemon_evolves_level']}"

    return string_to_append
