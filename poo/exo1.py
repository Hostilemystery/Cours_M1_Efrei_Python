"""  
 Créez une classe "De" qui simule le lancer d'un dé à six faces. Ajoutez une méthode pour
 lancer le dé et obtenir un nombre aléatoire entre 1 et 6.
"""

import random

class De:
    def __init__(self):
        self.faces = 6

    def lancer(self):
        return random.randint(1, self.faces)
de = De()
resultat = de.lancer()
print(resultat)
