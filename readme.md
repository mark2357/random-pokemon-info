# Random Pokemon Info
prints out random info about pokemon to the console
has thousands of different possible options
this uses the https://pokeapi.co/ API

## dependencies
python

requests
requests_cache

both requests and requests_cache can be installed using pip with the following commands
```
pip install requests
pip install requests_cache
```
as this library uses the https://pokeapi.co/ so unless the cache script has been fully run this library requires an internet connection


## pre-caching
you can pre-cache the endpoint data by running the 
this can be run by running the following from within a script
```
import random_pokemon_info

random_pokemon_info.pre_cache_all_used_endpoints()
```

WARNING this will take a long time to run as it's designed not send a continuous stream of requests to the API
This will also take a large amount of space on the disk (several hundred megabytes)


## available functions

### get_random_info
randomly calls one of the other info functions and returns a string containing random information about pokemom

```
import random_pokemon_info

random_pokemon_info.get_random_info()
```


### get_random_pokemon_ability_info
returns a string stating a possible ability of a pokemon

```
import random_pokemon_info

random_pokemon_info.get_random_info()
```


### get_random_pokemon_evolution_info
returns a string stating a pokemon and what it can evolve into or a single pokemon stating that it cannot evolve

```
import random_pokemon_info

random_pokemon_info.get_random_info()
```


### get_random_pokemon_generation_introduced_info
returns a string stating what generation a pokemon was introduced

```
import random_pokemon_info

random_pokemon_info.get_random_pokemon_generation_introduced_info()
```


### get_random_pokemon_height_info
returns a string stating a pokemon and it's height

```
import random_pokemon_info

random_pokemon_info.get_random_pokemon_height_info()
```


### get_random_pokemon_highest_stat_info
returns a string stating a pokemon and one of it's highest base stat values

```
import random_pokemon_info

random_pokemon_info.get_random_pokemon_highest_stat_info()
```


### get_random_pokemon_lowest_stat_info
returns a string stating a pokemon and one of it's lowest base stat values

```
import random_pokemon_info

random_pokemon_info.get_random_pokemon_lowest_stat_info()
```


### get_random_pokemon_type_info
returns a string stating a pokemon and it's type(s)

```
import random_pokemon_info

random_pokemon_info.get_random_pokemon_type_info()
```


### get_random_pokemon_type_weakness_or_resistance_info
returns a string stating a pokemon and one of it's weaknesses resistances or immunities

```
import random_pokemon_info

random_pokemon_info.get_random_pokemon_type_weakness_or_resistance_info()
```


### get_random_pokemon_weight_info
returns a string stating a pokemon and it's weight

```
import random_pokemon_info

random_pokemon_info.get_random_pokemon_weight_info()
```


### pre_cache_all_used_endpoints
goes through each possible endpoint that may be used by the module and caches the data in a local sqlite database 

parameters
`wait_time_between_requests` the time the function waits between requests, value shouldn't be zero as this may cause problems with web API

```
import random_pokemon_info

random_pokemon_info.pre_cache_all_used_endpoints(3)
```
