# Random Pokemon Info
prints out random info about pokemon to the console
has thousands of different possible options

## dependencies
python

requests
requests_cache

## pre-caching
you can pre-cache the endpoint data by running the cache_all_used_endpoints.py
this can be run by running the following command
'''
python ./cache_all_used_endpoints.py
'''

WARNING this will take a long time to run as it's designed not send a continuous stream of requests to the API
This will also take a large amount of space on the disk (several hundred megabytes)


## running
the script can be be run by using the following command

'''
python ./get_random_info.py
'''
