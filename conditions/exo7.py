""" 
Vérifier si un nombre saisi par l'utilisateur est pair ou non. Le programme demande à
l'utilisateur d'entrer un nombre, puis il vérifie si le nombre est pair ou impair. Si c'est le
cas, le programme affiche que le nombre est pair. Sinon, il affiche que le nombre n'est
pas pair.
Faites en sorte qu’on ne puisse entrer que des entiers

"""

nombre = int(input("entrer un nombre pair"))

print("Le nombre est pair" if nombre%2 else "Le nombre est impair")

