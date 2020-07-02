'''contains basic function for getting data from API endpoint'''
import requests
import requests_cache


def fetch_data_from_api(url):
    '''returns data from API endpoint'''

    # installs cache so it uses cached data
    requests_cache.install_cache()

    # Make a GET request to fetch the raw HTML content
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error status code is not 200 it's {response.status_code}")

    # uncomment if you want do display when data is from cache
    # if response.from_cache:
    #     print(f"request from {url} is from cache")
    # else:
    #     print(f"request from {url} is not from cache")

    # uninstalls cache incase module is used in application using requests that doesn't need caching
    requests_cache.uninstall_cache()

    content = response.text
    return content
