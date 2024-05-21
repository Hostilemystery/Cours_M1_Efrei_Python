""" 
Vous devez réaliser les tables de multiplications de “1, 2, 3, 5” et “8”.
>> Création d’une liste par table avec l’ensemble des résultats des multiplications
"""

liste = [1, 2, 3, 5, 8]
tables_multiplication = {}

for i in range(len(liste)):
    result = []
    for j in range(1, len(liste)):  
        result.append(liste[i] * j)
    tables_multiplication[liste[i]] = result

print(tables_multiplication)
