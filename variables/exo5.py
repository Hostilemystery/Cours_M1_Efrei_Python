""" 
Créer une variable qui détermine si une autre variable existe ou si elle n’existe pas elle
prend la valeur de 42 à la place. (aucune condition acceptée !).
"""
variable_a_verifier = 38

variable = locals().get('variable_a_verifier', 42)

print(variable)