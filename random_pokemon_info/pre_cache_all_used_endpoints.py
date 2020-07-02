'''contains function to pre caches used endpoints'''

import os
import time
import datetime
import json
import requests
import requests_cache


def pre_cache_all_used_endpoints(wait_time_between_requests):
    '''pre caches endpoints used by module'''

    # installs cache so it uses cached data
    requests_cache.install_cache()

    # these endpoints return lists of endpoints to cache
    # if name based is set to true then url uses the name of the resource instead of it's id
    # e.g. uses /pokemon/bulbasaur/ instead of /pokemon/1/
    # name based is used for types as they are retrieved by name not id
    endpoint_list_endpoints = [
        {'url':'https://pokeapi.co/api/v2/pokemon/?limit=1000', 'name_based': False},
        {'url':'https://pokeapi.co/api/v2/evolution-chain/?limit=500', 'name_based': False},
        {'url':'https://pokeapi.co/api/v2/pokemon-species/?limit=1000', 'name_based': False},
        {'url':'https://pokeapi.co/api/v2/type/', 'name_based': True},
    ]


    print(f'before starting caching cached {len(requests_cache.get_cache().responses)} endpoints')

    print('calculating total endpoints to cache (will take a few seconds)')

    url_cache_list = []

    # adds each endpoint that needs to be cached from each endpoint list
    for endpoint_list_url in endpoint_list_endpoints:
        response = requests.get(endpoint_list_url['url'])
        if response.status_code != 200:
            print(f"Error status code is not 200 it's {response.status_code}")
            continue

        data = json.loads(response.text)
        for item in data['results']:
            if endpoint_list_url['name_based'] == False:
                url_cache_list.append(item['url'])
            else:
                url = os.path.dirname(os.path.dirname(item['url'])) + '/' + item['name'] + '/'
                url_cache_list.append(url)

        time.sleep(wait_time_between_requests)


    # tries to determine the max time it will take to cache all the data
    time_data = datetime.timedelta(seconds=wait_time_between_requests * len(url_cache_list))
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
            time.sleep(wait_time_between_requests)

    print(f'after caching cached {len(requests_cache.get_cache().responses)} endpoints')


    # uninstalls cache incase module is used in application using requests that doesn't need caching
    requests_cache.uninstall_cache()
