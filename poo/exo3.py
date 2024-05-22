
"""  
 Créez une classe "JeuDePendu" où l'ordinateur choisit un mot et le joueur doit le deviner
 en proposant des lettres. Le jeu affiche le mot masqué avec les lettres correctement
 devinées.
"""

import random

class JeuDePendu:
    def __init__(self, liste_mots):
        self.liste_mots = liste_mots
        self.mot_secret = random.choice(liste_mots)
        self.lettres_devinees = []
        self.lettres_incorrectes = []

    def deviner_lettre(self, lettre):
        if lettre in self.lettres_devinees:
            return "Vous avez déjà deviné cette lettre !"
        elif lettre in self.lettres_incorrectes:
            return "Vous avez déjà essayé cette lettre et elle est incorrecte !"
        elif lettre not in self.mot_secret:
            self.lettres_incorrectes.append(lettre)
            return "Cette lettre n'est pas dans le mot !"
        else:
            self.lettres_devinees.append(lettre)
            if len(self.lettres_devinees) == len(set(self.mot_secret)):
                return "Bravo, vous avez trouvé le mot !"
            else:
                return "Bien joué, cette lettre est dans le mot !"

    def afficher_mot(self):
        mot_affiche = ""
        for lettre in self.mot_secret:
            if lettre in self.lettres_devinees:
                mot_affiche += lettre
            else:
                mot_affiche += "_"
        return mot_affiche


liste_mots = ["chat", "chien", "oiseau", "poisson"]
jeu = JeuDePendu(liste_mots)

while True:
    proposition = input("Entrez une lettre : ").lower()
    resultat = jeu.deviner_lettre(proposition)
    print(resultat)
    print(jeu.afficher_mot())
    if resultat == "Bravo, vous avez trouvé le mot !":
        break
