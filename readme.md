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
you can pre-cache the endpoint data by running the cache_all_used_endpoints.py
this can be run by running the following command
```
python ./cache_all_used_endpoints.py
```

WARNING this will take a long time to run as it's designed not send a continuous stream of requests to the API
This will also take a large amount of space on the disk (several hundred megabytes)


## running
the script can be be run by using the following command

```
python ./test.py
```
