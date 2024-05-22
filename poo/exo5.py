""" 
 Créez une classe "Joueur" avec un solde initial et une classe "Case" avec un coût.
 Implémentez un jeu de Monopoly où les joueurs lancent un dé, se déplacent sur une case,
 et paient le coût de la case (prix du loyer). Il est possible d’utiliser l’exercice 1 en important la
 class jeux de dés
"""

import random
from exo1 import De


class Joueur:
    def __init__(self, nom, solde_initial):
        self.nom = nom
        self.solde = solde_initial
        self.position = 0 # Ajout de l'attribut position

    def payer_loyer(self, montant):
        self.solde -= montant

class Case:
    def __init__(self, nom, cout):
        self.nom = nom
        self.cout = cout

    def afficher_infos(self):
        print(f"{self.nom} - Loyer : {self.cout}")

class Plateau:
    def __init__(self):
        self.cases = [
            Case("Départ", 0),
            Case("Rue de la Paix", 20),
            Case("Chance", 0),
            Case("Boulevard des Capucines", 30),
            Case("Caisse de communauté", 0),
            Case("Rue de Rivoli", 40),
            Case("Gare du Nord", 50),
            Case("Rue Saint-Honoré", 60),
            Case("Chance", 0),
            Case("Avenue de l'Opéra", 70),
            # ... ajoutez autant de cases que vous voulez ...
        ]

    def obtenir_case(self, position):
        return self.cases[position % len(self.cases)]

class Jeu:
    def __init__(self, joueurs, solde_initial):
        self.joueurs = joueurs
        self.solde_initial = solde_initial
        self.plateau = Plateau()
        self.de = De()

    def jouer(self):
        for tour in range(1, 100):
            print(f"\n--- Tour n°{tour} ---")
            for joueur in self.joueurs:
                position_initiale = self.plateau.obtenir_case(joueur.position).nom
                print(f"{joueur.nom} est sur la case {position_initiale}")
                resultat_de = self.de.lancer()
                print(f"Il a obtenu {resultat_de} avec le dé")
                joueur.position += resultat_de
                case = self.plateau.obtenir_case(joueur.position)
                print(f"Il se déplace sur la case {case.nom}")
                if case.cout > 0:
                    print("Il doit payer le loyer :")
                    case.afficher_infos()
                    joueur.payer_loyer(case.cout)
                print(f"Son nouveau solde est de {joueur.solde}")

joueurs = [
    Joueur("Joueur 1", 1000),
    Joueur("Joueur 2", 1000),
]

jeu = Jeu(joueurs, 1000)
jeu.jouer()
