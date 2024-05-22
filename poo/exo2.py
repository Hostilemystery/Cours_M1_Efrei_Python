""" 
 Créez une classe "JeuDeDevinette" où l'ordinateur choisit un nombre aléatoire entre 1 et
 100. Le joueur doit deviner ce nombre. La classe doit fournir des indices si la proposition est
 trop grande ou trop petite.
"""

import random

class JeuDeDevinette:
    def __init__(self):
        self.nombre_secret = random.randint(1, 100)

    def deviner(self, proposition):
        if proposition < self.nombre_secret:
            return "C'est plus !"
        elif proposition > self.nombre_secret:
            return "C'est moins !"
        else:
            return "Bravo, vous avez trouvé !"

jeu = JeuDeDevinette()

while True:
    proposition = int(input("Entrez votre proposition : "))
    resultat = jeu.deviner(proposition)
    print(resultat)
    if resultat == "Bravo, vous avez trouvé !":
        break
