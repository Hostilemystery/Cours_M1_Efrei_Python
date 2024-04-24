""" 
Créez une variable “rand” et calculez un nombre aléatoire entre “1” et “42” si le chiffre
est égal à “42” retourner “true”
"""
import random #On importe la librerie random


rand = random.randrange(1,42) 

result =  rand==42

print(f"{rand} = 42 : {result}")
