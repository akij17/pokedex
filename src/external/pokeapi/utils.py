



# [{'slot': 2, 'type': {'name': 'flying', 'url': 'https://pokeapi.co/api/v2/type/3/'}}, {'slot': 1, 'type': {'name': 'fire', 'url': 'https://pokeapi.co/api/v2/type/10/'}}]
# [{'slot': 1, 'type': {'name': 'fire', 'url': 'https://pokeapi.co/api/v2/type/10/'}}]
def extract_types(type_data):
    if len(type_data) == 1:
        return type_data[0]['type']['name'], None
    else:
        type1 = [t for t in type_data if t['slot'] == 1]
        type2 = [t for t in type_data if t['slot'] == 2]
        return type1[0]['type']['name'], type2[0]['type']['name']
