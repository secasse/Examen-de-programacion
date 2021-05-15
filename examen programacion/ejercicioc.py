import json
import requests
import random

def get_carter_by_id(id):
    respuesta = requests.get('https://swapi.dev/api/people/'+str(id))
    if respuesta.status_code == 200:
        dic = json.loads(respuesta.text)
        return dic


def get_random_character():
    randomCharacterId = random.randrange(1, 82, 2)
    character = get_carter_by_id(randomCharacterId)
    return character

def main():
    personaje1 = get_random_character()
    personaje2 = get_random_character()

    peliculas = personaje1 if len(personaje1['films']) > len(personaje2['films']) else personaje2


    print('El que estuvo en mas peliculas es: ' + str(peliculas.get('name')))
        
main()