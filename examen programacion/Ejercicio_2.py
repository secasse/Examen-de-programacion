
from consumo_api import get_all_sw_characters
personajes_sw = get_all_sw_characters()

def ordenar (item):
    return (item['name'])


personajes_sw.sort(key=ordenar)

for index, character in enumerate(personajes_sw):
    print(character['name'], character['species'], character['homeworld'])

for character in personajes_sw:
    if(len(character['films'])==6):
        print('Los que estuvieron en 6 peliculas fueron:', character ['name'])
