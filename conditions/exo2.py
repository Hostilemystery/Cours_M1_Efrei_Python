""" 
Créer un algorithme qui retourne : “Cool” quand la valeur est comprise entre 0 et 10.
“Tepid” quand la valeur est comprise entre 11 et 20. “Warm” quand la valeur est
comprise entre 21 et 30. Cette condition devra utiliser une variable “rand” avec un
nombre aléatoire compris entre 0 et 30

"""

import random

valeur  = random.randint(0,30)

print(valeur," Warm " if valeur >20 else "Tepid" if valeur>10 else "Cool")