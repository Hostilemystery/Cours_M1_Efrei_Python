"""
Écrivez un programme qui génère et affiche le motif suivant en utilisant des boucles
imbriquées : * ** *** **** *****
"""

var = ""
for i in range(1,6):
    var += "*"*i+" "
print(var)

#Meilleur alternative 
print(' '.join(list(map(lambda x : x*'*', range(1,6)))))
    
