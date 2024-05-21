"""
Écrivez un programme qui génère et affiche le motif suivant en utilisant des boucles
imbriquées : * ** *** **** *****
"""

var = ""
for i in range(0,6):
    var += "*"*i+" "
print(var)