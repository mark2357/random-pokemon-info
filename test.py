'''used to test the module'''

# this file doesn't currently test all possible outcomes of each function
# doesn't test teh pre_cache_all_used_endpoints as it can take hours

import random_pokemon_info

print('starting testing')
print('---')

print('testing get_random_info')
print(random_pokemon_info.get_random_info())

print('testing get_random_pokemon_ability_info')
print(random_pokemon_info.get_random_pokemon_ability_info())

print('testing get_random_pokemon_evolution_info')
print(random_pokemon_info.get_random_pokemon_evolution_info())

print('testing get_random_pokemon_generation_introduced_info')
print(random_pokemon_info.get_random_pokemon_generation_introduced_info())

print('testing get_random_pokemon_height_info')
print(random_pokemon_info.get_random_pokemon_height_info())

print('testing get_random_pokemon_highest_stat_info')
print(random_pokemon_info.get_random_pokemon_highest_stat_info())

print('testing get_random_pokemon_lowest_stat_info')
print(random_pokemon_info.get_random_pokemon_lowest_stat_info())

print('testing get_random_pokemon_type_info')
print(random_pokemon_info.get_random_pokemon_type_info())

print('testing get_random_pokemon_type_weakness_or_resistance_info')
print(random_pokemon_info.get_random_pokemon_type_weakness_or_resistance_info())

print('testing get_random_pokemon_weight_info')
print(random_pokemon_info.get_random_pokemon_weight_info())

print('---')
print('finished testing')
