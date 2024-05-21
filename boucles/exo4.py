""" 
 Vous devez créer une variable avec l’objet suivant {“a”: 42, “b”: 42, “c”: 42, “d”: 42}.
 Vous devrez parcourir chaque key et faire la multiplication de la valeur précédente par la
 nouvelle (accumulateur) sauf pour la lettre ‘d’ ou vous devrez faire une soustraction de
 42. Le calcul retournera “74046”

"""


data = {"a": 42, "b": 42, "c": 42, "d": 42}

accumulator = data["a"]

keys = list(data.keys())
for key in keys[1:]:
    if key == 'd':
        accumulator -= data[key]
    else:
        accumulator *= data[key]

print(accumulator)
