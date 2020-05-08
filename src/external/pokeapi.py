import requests

BASE_URL = 'http://pokeapi.co/api/v2'
ENDPOINTS = {
    'pokemon-data' : 'pokemon'
}

def call_api(endpoint, query):
    url = BASE_URL + '/' + endpoint + '/' + query

    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        return None

def pokemon_data(pokemon_name):
    response = call_api(ENDPOINTS['pokemon-data'], pokemon_name)
    return response.json()
