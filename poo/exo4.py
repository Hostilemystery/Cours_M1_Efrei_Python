""" 
Créez une classe "Carte" avec des attributs pour la valeur et la couleur. Créez une classe
 "PaquetDeCartes" qui peut être mélangée et distribuée
"""

import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class PaquetDeCartes:
    def __init__(self):
        self.couleurs = ["Coeur", "Carreau", "Trefle", "Pique"]
        self.valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        self.cartes = [Carte(valeur, couleur) for valeur in self.valeurs for couleur in self.couleurs]

    def meler(self):
        random.shuffle(self.cartes)

    def distribuer(self):
        if len(self.cartes) == 0:
            return "Plus de cartes dans le paquet !"
        else:
            return self.cartes.pop(0)

paquet = PaquetDeCartes()
paquet.meler()

for i in range(5):
    carte = paquet.distribuer()
    print(carte)
