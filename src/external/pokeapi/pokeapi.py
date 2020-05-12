import src.external.pokeapi.api as api
import src.external.pokeapi.utils as utils

def build_pokemon_list_cache():
    api.build_pokemon_list_cache()

def get_pokemon_type(pokemon_name):
    # check if available in cache
    # if not then call the api
    type_data = api.pokemon_data(pokemon_name)['types']

    return utils.extract_types(type_data)