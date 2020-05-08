class PokemonData():
    def __init__(self, pokemon_name, pokemon_species, pokemon_type, pokemon_evolution):
        self.pokemon_name = pokemon_name
        self.pokemon_species = pokemon_species
        self.pokemon_type = pokemon_type
        self.pokemon_evolution = pokemon_evolution
    
    def print_data(self):
        print('Name:', self.pokemon_name)
        print('Species:', self.pokemon_species)
        print('Type:', self.pokemon_type.print_data())
        print('Evolution:', self.pokemon_evolution)

class PokemonType():
    def __init__(self, type1, type2):
        self.type1 = type1
        self.type2 = type2 
    
    def print_data(self):
        if self.type2 == None:
            print('Type:', self.type1)
        else:
            print('Type:', self.type1, self.type2)