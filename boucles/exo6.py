
"""
(Trie à bulle) Vous devez réaliser un algo qui vous permettra de trier un tableau “nbr”
en ordre croissant par exemple si j’ai “[5, 4, 3, 2, 1]” le résultat sera “[1, 2, 3, 4, 5]”.
Vous n’avez pas le droit d’utiliser de fonction.
"""

nbr = [12,4,78,6,5]

for i in nbr:
    for j in range(len(nbr)-1):
        if nbr[j] > nbr[j+1]:
            nbr[j], nbr[j+1] = nbr[j+1], nbr[j]
                
print(nbr)