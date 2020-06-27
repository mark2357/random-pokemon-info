'''contains basic function for getting data from API endpoint'''
import requests
import requests_cache

requests_cache.install_cache()

def fetch_data_from_api(url):
    '''returns data from API endpoint'''
    # Make a GET request to fetch the raw HTML content
    request = requests.get(url)

    # uncomment if you want do display when data is from cache
    # if request.from_cache:
    #     print(f"request from {url} is from cache")
    # else:
    #     print(f"request from {url} is not from cache")

    content = request.text
    return content
