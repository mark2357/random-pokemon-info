'''pre caches used endpoints'''

import time
import datetime
import json
import requests
import requests_cache

requests_cache.install_cache()

# these endpoints return lists of endpoints to cache
endpoint_list_endpoints = [
    'https://pokeapi.co/api/v2/pokemon/?limit=1000',
    'https://pokeapi.co/api/v2/evolution-chain/?limit=500',
    'https://pokeapi.co/api/v2/pokemon-species/?limit=1000',
    'https://pokeapi.co/api/v2/type/'

]

DELAY_TIME_IN_SEC = 3


print(f'before starting caching cached {len(requests_cache.get_cache().responses)} endpoints')

print('calculating total endpoints to cache (will take a few seconds)')

url_cache_list = []

# adds each endpoint that needs to be cached from each endpoint list
for endpoint_list_url in endpoint_list_endpoints:
    response = requests.get(endpoint_list_url)
    if response.status_code != 200:
        print(f"Error status code is not 200 it's {response.status_code}")
        continue

    data = json.loads(response.text)
    for item in data['results']:
        url_cache_list.append(item['url'])

    time.sleep(DELAY_TIME_IN_SEC)


# tries to determine the max time it will take to cache all the data
time_data = datetime.timedelta(seconds=DELAY_TIME_IN_SEC * len(url_cache_list))
print(f'warning caching can take around {time_data}')


# caches each url
for url in url_cache_list:
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error status code is not 200 it's {response.status_code}")
    if response.from_cache:
        print(f'url: {url} was previously cached')
    else:
        print(f"url: {url} wasn't previously cached")
        time.sleep(DELAY_TIME_IN_SEC)

print(f'after caching cached {len(requests_cache.get_cache().responses)} endpoints')
