""" 
 Vous devez créer une liste de 1 à 10 et multiplier les résultats de la table de “5” (vous
 n'avez le droit d’utiliser que les String). Utilisez une boucle For.
 >> Création de listes de strings indiquant :
 5 x 1=5
 5 x 2=10
 … 
"""
table_multiplication  = []
nbre = 5
for i in  range(1,11):
    resultat = f"{nbre} x {i} = {nbre}*{i}"
    table_multiplication.append(resultat)
print(table_multiplication)
