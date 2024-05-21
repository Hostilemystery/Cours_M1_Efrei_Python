""" 
 Même exercice que le 2 avec une boucle “while” avec “true” comme valeur de
 condition. Faites une incrémentation dans un print() avec la table de multiplication par
 “5”
"""

i = 1
table_multiplication  = []
nbre = 5

while True:
    if i > 10:
        break
    print(f"{nbre} x {i} = {nbre * i}")
    i += 1