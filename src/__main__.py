import sys
import src.external.pokeapi.pokeapi as pokeapi

valid_operations = {
    'weak'
}

def main():
    arg_size = len(sys.argv)
    pokeapi.build_pokemon_list_cache()


if __name__ == 'main':
    main()