class PokemonData():
    def __init__(self, pokemon_id, pokemon_name, pokemon_type, pokemon_evolution, pokemon_ability, pokemon_hidden_ability):
        self.pokemon_id = pokemon_id
        self.pokemon_name = pokemon_name
        self.pokemon_type = pokemon_type
        self.pokemon_evolution = pokemon_evolution
        self.pokemon_ability = pokemon_ability
        self.pokemon_hidden_ability = pokemon_hidden_ability
    
    def print_data(self):
        print("ID:", self.pokemon_id)
        print('Name:', self.pokemon_name)
        print('Type:', self.pokemon_type.print_data())
        print('Ability:', self.pokemon_ability)
        print('Hidden Ability', self.pokemon_hidden_ability)
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