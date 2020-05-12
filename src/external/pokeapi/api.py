import requests
import os
import json
import pickle

BASE_URL = 'http://pokeapi.co/api/v2'
ENDPOINTS = {
    'pokemon-data' : 'pokemon'
}

def build_pokemon_list_cache():
    current_path = os.path.dirname(os.path.abspath(__file__))
    filename = current_path + '/cache/pokemon_list'
    if os.path.isfile(filename):
        pass
    else:
        url = BASE_URL + '/pokemon/?offset=0&limit=2000'
        r = requests.get(url).text
        data = json.loads(r)

        pokemon_list = list()

        poke_no = int(data['count'])

        for i in range(0, poke_no):
            pokemon_list.append(data['results'][i]['name'])

        poke_list = set(pokemon_list)
        with open(filename, 'wb') as fp:
            pickle.dump(poke_list, fp)

def dump_json_to_disk(endpoint, name, json_file):
    current_path = os.path.dirname(os.path.abspath(__file__))
    filename = current_path + '/cache/' + endpoint + '/' + name 
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as file:
        json.dump(json_file, file)

def fetch_from_cache(endpoint, name):
    current_path = os.path.dirname(os.path.abspath(__file__))
    filename = current_path + '/cache/' + endpoint + '/' + name
    if os.path.isfile(filename):
        file = open(filename)
        return json.load(file)
    else:
        return None

def call_api(endpoint, query):
    url = BASE_URL + '/' + endpoint + '/' + query

    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        return None

def pokemon_data(pokemon_name):
    required_endpoint = ENDPOINTS['pokemon-data']
    cache_response = fetch_from_cache(required_endpoint, pokemon_name)
    if cache_response != None:
        return cache_response
    else:
        response = call_api(ENDPOINTS['pokemon-data'], pokemon_name).text
        json_file = json.loads(response)
        dump_json_to_disk(ENDPOINTS['pokemon-data'], pokemon_name, json_file)
        return json_file

