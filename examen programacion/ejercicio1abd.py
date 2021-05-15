from random import randint
from pruebaaa import altura
from consumo_api import get_charter_by_id
from pruebaaa import peso






id1 = randint(1,83),
personaje0 = get_charter_by_id(9)


id2 = randint(1,83),
personaje1 = get_charter_by_id(4)




if (altura(personaje0) >= altura(personaje1)) :
   print ("El personaje mas alto es",personaje1["name"],"la altura es", altura(personaje1))

else:
    print ("El personaje mas alto es",personaje0["name"],"la altura es", altura(personaje1))


if (peso(personaje0)) >= (peso(personaje1)):

   print ("El personaje mas pesado es",personaje0["name"],"el peso es", altura(personaje1))

else:
    print ("El personaje mas pesado es",personaje1["name"],"el peso es", altura(personaje0))



if (personaje0 == "Yoda" or personaje1 == "Grievous" or  personaje0 == "Grievous" or personaje1 == "Yoda") :
    print(personaje0)
    print(personaje1)