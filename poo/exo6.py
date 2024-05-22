"""  
Créez deux classes "Personnage" avec des attributs tels que la santé et les dégâts.
 Implémentez un jeu de combat où deux personnages s'affrontent jusqu'à ce que l'un d'eux
 n'ait plus de santé. Il y aura une boucle de jeu au tour par tour.
"""

import random

class Personnage:
    def __init__(self, nom, sante, degats):
        self.nom = nom
        self.sante = sante
        self.degats = degats

    def attaquer(self, personnage):
        degats_infliges = random.randint(1, self.degats)
        personnage.sante -= degats_infliges
        print(f"{self.nom} inflige {degats_infliges} points de dégâts à {personnage.nom}")

    def est_vivant(self):
        return self.sante > 0

class Jeu:
    def __init__(self, personnage1, personnage2):
        self.personnage1 = personnage1
        self.personnage2 = personnage2

    def jouer(self):
        tour = 1
        while self.personnage1.est_vivant() and self.personnage2.est_vivant():
            print(f"\n--- Tour n°{tour} ---")
            self.personnage1.attaquer(self.personnage2)
            if self.personnage2.est_vivant():
                self.personnage2.attaquer(self.personnage1)
            tour += 1

        if self.personnage1.est_vivant():
            print(f"{self.personnage1.nom} a gagné !")
        else:
            print(f"{self.personnage2.nom} a gagné !")

# Création des personnages
personnage1 = Personnage("Guerrier", 100, 20)
personnage2 = Personnage("Mage", 80, 30)

# Création du jeu et lancement de la partie
jeu = Jeu(personnage1, personnage2)
jeu.jouer()
