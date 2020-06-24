'''contains basic function for getting data from API endpoint'''
import requests
import requests_cache

requests_cache.install_cache()

def fetch_data_from_api(url):
    '''returns data from API endpoint'''
    # Make a GET request to fetch the raw HTML content
    content = requests.get(url).text
    return content
