""" 
 Si vous avez réussi le précédent exercice, vous pouvez essayer d’afficher cette structure
"""
hauteur = 10

for i in range(1, hauteur + 1):
    espaces = ' ' * (hauteur - i)
    parantheses = '[' * i + ' '  + ']' * i
    print(espaces + parantheses)


#Alternative

for i in range(1, hauteur + 1):
    parantheses = '[' * i + ' '  + ']' * i
    print(parantheses.center(10*3))