'''pre caches used endpoints'''

import time
import datetime
import requests
import requests_cache

endpoints = [
    {'url': 'https://pokeapi.co/api/v2/pokemon/', 'range-min': 1, 'range-max': 808},
    {'url': 'https://pokeapi.co/api/v2/evolution-chain/', 'range-min': 1, 'range-max': 428},
    {'url': 'https://pokeapi.co/api/v2/pokemon-species/', 'range-min': 1, 'range-max': 808},
    {'url': 'https://pokeapi.co/api/v2/type/', 'range-min': 1, 'range-max': 19}
]

DELAY_TIME_IN_SEC = 3
TOTAL_ENDPOINTS = 0
for endpoint in endpoints:
    TOTAL_ENDPOINTS += endpoint['range-max'] - endpoint['range-min']

time_data = datetime.timedelta(seconds=DELAY_TIME_IN_SEC * TOTAL_ENDPOINTS)

print(f'before startingcaching cached {len(requests_cache.get_cache().responses)} endpoints')
print(f'warning caching can take around {time_data}')
for endpoint in endpoints:
    for x in range(endpoint['range-min'], endpoint['range-max']):
        full_url = f"{endpoint['url']}{x}"
        response = requests.get(full_url)
        if response.from_cache:
            print(f'url: {full_url} has already been cached')
        else:
            print(f'url: {full_url} has not been cached')
            time.sleep(DELAY_TIME_IN_SEC)

print(f'after caching cached {len(requests_cache.get_cache().responses)} endpoints')
