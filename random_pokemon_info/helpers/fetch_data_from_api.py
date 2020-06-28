'''contains basic function for getting data from API endpoint'''
import requests
import requests_cache

requests_cache.install_cache()

def fetch_data_from_api(url):
    '''returns data from API endpoint'''
    # Make a GET request to fetch the raw HTML content
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error status code is not 200 it's {response.status_code}")

    # uncomment if you want do display when data is from cache
    # if request.from_cache:
    #     print(f"request from {url} is from cache")
    # else:
    #     print(f"request from {url} is not from cache")

    content = response.text
    return content
