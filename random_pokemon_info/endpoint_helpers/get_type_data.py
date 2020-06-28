'''contains function for retreving pokemon type API Data'''

import json

from ..helpers.fetch_data_from_api import fetch_data_from_api

def get_type_data(type_name):
    '''returns type data from the given type'''

    data = json.loads(fetch_data_from_api(f'https://pokeapi.co/api/v2/type/{type_name}'))
    return data


def get_type_weaknesses_and_resistances(type_name):
    '''returns weakness, resistane and immunity damage multipliers for the given type'''

    damage_relations = get_type_data(type_name)['damage_relations']

    damage_multipliers = dict()

    damage_multipliers = add_type_to_damage_multipliers(damage_multipliers, damage_relations)

    return damage_multipliers


def get_duel_type_weaknesses_and_resistances(type_name_1, type_name_2):
    '''returns weakness, resistane and immunity damage multipliers for the given 2 types'''

    damage_relations_1 = get_type_data(type_name_1)['damage_relations']
    damage_relations_2 = get_type_data(type_name_2)['damage_relations']

    damage_multipliers = dict()

    damage_multipliers = add_type_to_damage_multipliers(damage_multipliers, damage_relations_1)
    damage_multipliers = add_type_to_damage_multipliers(damage_multipliers, damage_relations_2)

    # works out if types need to be removed
    types_to_remove = []
    for type_name, type_multiplier in damage_multipliers.items():
        if type_multiplier == 1:
            types_to_remove.append(type_name)

    # removes types
    for type_name in types_to_remove:
        damage_multipliers.pop(type_name)

    return damage_multipliers


def add_type_to_damage_multipliers(damage_multipliers, damage_relations):
    '''uses the type relations and adds or recalculates the new damage multiplier'''

    # if the type has weaknesses
    if 'double_damage_from' in damage_relations:

        # for each type
        for double_damage_type in damage_relations['double_damage_from']:
            double_damage_type_name = double_damage_type['name']

            # if the type already exists
            if double_damage_type_name in damage_multipliers:
                damage_multipliers[double_damage_type_name] = 2 * damage_multipliers[double_damage_type_name]
            else:
                damage_multipliers[double_damage_type_name] = 2


    # if the type has resistances
    if 'half_damage_from' in damage_relations:

        # for each type
        for half_damage_type in damage_relations['half_damage_from']:
            half_damage_type_name = half_damage_type['name']

            # if the type already exists
            if half_damage_type_name in damage_multipliers:
                damage_multipliers[half_damage_type_name] = 0.5 * damage_multipliers[half_damage_type_name]
            else:
                damage_multipliers[half_damage_type_name] = 0.5


    if 'no_damage_from' in damage_relations:

        # for each type
        for no_damage_type in damage_relations['no_damage_from']:
            no_damage_type_name = no_damage_type['name']

            damage_multipliers[no_damage_type_name] = 0

    return damage_multipliers
