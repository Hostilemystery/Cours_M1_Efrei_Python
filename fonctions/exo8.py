""" 
  Vous devez réaliser une fonction capable de calculer la suite de fibonacci à partir d’une
 taille limite fix en argument pour limiter la taille de la suite. Vous deverez réaliser
 obligatoirement une recursive.
 Par exemple si je donne 5 en argument la resultat sera le suivant :
 [1, 1, 2, 3, 5]

"""
suite = []
def fibonacci(nbr):
    if nbr < 0:
        return "Entrer un nombre superieur a 0"
    elif nbr == 0:
        return 0
    
    elif nbr == 1 or nbr == 2:
        return 1
    else : 
        result = fibonacci(nbr-1)+fibonacci(nbr-2)
        suite.append(result)
        return suite
    
print(fibonacci(5))



