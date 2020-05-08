import models
import external.pokeapi as pokeapi

def get_pokemon_basic_data(pokemon_name):
    api_response = pokeapi.pokemon