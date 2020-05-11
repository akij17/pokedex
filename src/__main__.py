import sys
import src.external.pokeapi.pokeapi as pokeapi

def main():
    print("Pokemon:", sys.argv[1])
    print("Type:", pokeapi.get_pokemon_type(sys.argv[1]))

if __name__ == 'main':
    main()