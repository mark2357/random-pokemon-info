'''contains function that returns string stating random pokemon name and it's type or types'''

from endpoint_helpers.get_pokemon_data import get_random_pokemon_data

def get_random_pokemon_type_string():
    '''returns string stating random pokemon name and it's type or types'''
    data = get_random_pokemon_data()
    name = data['name']
    types = data['types']

    # single type pokemon
    if len(types) == 1:
        type_name = types[0]['type']['name']
        return f'{name} is a {type_name} type pokemon'

    # double type pokemon
    elif len(types) == 2:
        type_name_1 = types[0]['type']['name']
        type_name_2 = types[1]['type']['name']

        return f'{name} is a {type_name_1}, {type_name_2} type pokemon'

    # shouldn't occur
    return None
